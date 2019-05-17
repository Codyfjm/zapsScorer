# -*- coding: utf-8 -*-
'''
The database structure. flask db uses this to auto-generate the db.
And the server code uses this to operate the db.
'''

# core imports

from json import loads as json_loads, dumps as json_dumps
import pickle
import random

# framework imports

from flask import jsonify
from flask_login import UserMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm.collections import attribute_mapped_collection
from werkzeug.security import generate_password_hash, check_password_hash

# app imports

from mjserver import db, login, BASE_DIR

# initialisation

with open(str(BASE_DIR / 'wordlist.pickle'), 'rb') as wordlist_file:
    wordlist = pickle.load(wordlist_file)

wordlist_len = len(wordlist)

class User(db.Model, UserMixin):
    '''
    Currently we work on the basis that every registered player has a login, and
    every registered login is a (potential) player. So this class is used
    both for players and for website logins.
    '''
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(255))
    email = db.Column(db.Unicode(255), unique=True)
    username = db.Column(db.Unicode(255), unique=True)
    login_count = db.Column(db.Integer)
    pin = db.Column(db.Integer)
    password_hash = db.Column(db.String(128))
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean(), default=True)
    email_confirmed = db.Column(db.Boolean(), default=False)

    games = association_proxy('played_games', 'game')
    scores = association_proxy('played_games', 'score')
    places = association_proxy('played_games', 'place')

    def __repr__(self):
        ''' just for pretty printing '''
        return '<User {}>'.format(self.username)

    @classmethod
    def check_token(cls, token):
        return cls.query.filter_by(token=token).first()

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def create_token(self):
        ''' provide random 4-word sequence for logins '''
        token = ''
        sep = ''
        for idx in random.sample(range(wordlist_len), 4):
            token += sep + wordlist[idx]
            sep = ' '
        self.token = token
        db.session.commit()

    def gdpr_dump(self):

        keys = [
            'id', 'token', 'email', 'username', 'login_count', 'pin',
            'password_hash', 'last_login_at', 'current_login_at',
            'login_count', 'active', 'email_confirmed']

#    games = association_proxy('played_games', 'game')
#    scores = association_proxy('played_games', 'score')
#    places = association_proxy('played_games', 'place')

        out = {}
        for key in keys:
            out[key] = str(getattr(self, key))

        out['games'] = []
        for game in self.games:
            out['games'].append(game.json)

        return jsonify(out)

    @classmethod
    def get_all_usernames(cls):
        query = db.session.query(cls.id, cls.username).filter_by(active=True).order_by(cls.username)
        return query.all()

    def get_id(self):
        return str(self.id)

    def get_token(self):
        '''
        issue an authentication token for logins that is a random 4-word sequence
        that lasts 84 days, and store it
        with the user in the database. Renew it if there's less than 28 days life
        left on it.
        '''
        if not self.token :
            self.create_token()

        return self.token

    def is_active(self):
        return self.active

    def merge_with(self, other):
        '''
        Merge another user into this one. Note that this will currently
        only be used from the shell, as it makes irreversible changes
        that could really mess things up
        '''
        games_to_move = []
        for game in other.games:
            games_to_move.append(game)

        for game in games_to_move:
            user_game = UsersGames.query.filter_by(user_id=other.id, game_id=game.id).first()
            user_game.player = self
            game_json = json_loads(game.json)
            for player in game_json['players']:
                if player['user_id'] == other.id:
                    player['user_id'] = self.id
                    player['name'] = self.username

            game.json = json_dumps(game_json)
            db.session.commit()

        db.session.delete(other)
        db.session.commit()


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def set_pin(self, pin):
        self.pin = pin

    def to_dict(self):
        pass


@login.user_loader
def load_user(user_id):
    ''' get user for a given id '''
    try:
        return User.query.get(int(user_id))
    except:
        return None


class Game(db.Model):
    '''
    The heart of the database: an individual game record
    '''
    __tablename__ = 'game'
    id = db.Column(db.Unicode(255), primary_key=True)
    description = db.Column(db.UnicodeText())
    json = db.Column(db.UnicodeText())
    log = db.Column(db.UnicodeText())
    public = db.Column(db.Boolean())
    started = db.Column(db.DateTime())
    last_updated = db.Column(db.Float())
    is_active = db.Column(db.Boolean())

    players = association_proxy('games_players', 'player')
    player_names = association_proxy('games_players', 'player.username')
    scores = association_proxy('games_players', 'score')
    places = association_proxy('games_players', 'place')
    usersgames = db.relationship('UsersGames')

    def get_score_table(self):
        json = json_loads(self.json)
        if 'deltas' not in json['hands'][-1]:
            del json['hands'][-1]

        return json


#%% docs at http://docs.sqlalchemy.org/en/latest/orm/extensions/associationproxy.html

class UsersGames(db.Model):
    ''' this maps users to games, and provides the score and placement '''
    __tablename = 'user_game'
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.id'), primary_key=True)
    game_id = db.Column('game_id', db.Unicode(255), db.ForeignKey('game.id'), primary_key=True)
    score = db.Column(db.Integer())
    place = db.Column(db.Integer())

    player = db.relationship(
        User,
        backref=db.backref('played_games', lazy='dynamic', cascade="all, delete-orphan")
    )

    game = db.relationship(
        Game,
        backref=db.backref(
            'games_players',
            lazy='dynamic',
            cascade="all, delete-orphan",
            collection_class=attribute_mapped_collection("place"),
        ),
    )

    def __init__(self, user=None, game=None, score=-9999, place=-1):
        self.user = user
        self.game = game
        self.score = score
        self.place = place

#%%

User.usersgames = db.relationship('UsersGames')