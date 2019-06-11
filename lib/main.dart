/// The ZAPS Mahjong Scorer, in Flutter
///
/// This file only assigns top-level routes and the store

// https://www.dartlang.org/guides/language/effective-dart/documentation#doc-comments

//   onLongPress

// core imports

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

// third-party imports
import 'package:flutter_redux/flutter_redux.dart';

//

// imports from this app
import 'gamedb.dart';
import 'gameflow.dart';
import 'games.dart';
import 'hands.dart';
import 'hanfu.dart';
import 'help.dart';
import 'io.dart';
import 'players.dart';
import 'settings.dart';
import 'scoresheet.dart';
import 'store.dart';
import 'utils.dart';
import 'welcome.dart';
import 'whodidit.dart';
import 'yaku.dart';

void main() {
  SystemChrome.setSystemUIOverlayStyle(SystemUiOverlayStyle(
    statusBarColor: Colors.black, //top bar color
    statusBarIconBrightness: Brightness.light, //top bar icons
    systemNavigationBarColor: Colors.black, //bottom bar color
    systemNavigationBarIconBrightness: Brightness.light, //bottom bar icons
  ));

  initPrefs().then((_) {
    GLOBAL.playersListUpdated = !store.state.preferences['useServer'];
    GameDB db = GameDB();
    db.initDB().then((_) {
      db.listPlayers().then((_) {
        db.updatePlayersFromServer(); // this is async IO, and we must NOT wait for it here
        db.setLastGame().then((_) {
          SystemChrome.setPreferredOrientations([DeviceOrientation.portraitUp])
              .then((_) => runApp(ScorerApp()));
        });
      });
    });
  });
}

class ScorerApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return StoreProvider<Game>(
      // Pass the store to the StoreProvider. Any ancestor `StoreConnector`
      // Widgets will find and use this value as the `Store`.
      store: store,
      child: StoreConnector<Game, String>(
        converter: (store) => store.state.preferences['backgroundColour'],
        builder: (BuildContext context, String color) {
          return MaterialApp(
            initialRoute: ROUTES.hands,
            navigatorKey: USING_IO ? IO.httpLogger.getNavigatorKey() : null,
            title: "ZAPS Mahjong Scorer",
            theme: ThemeData(
              primaryColor: Colors.deepPurple[900],
              scaffoldBackgroundColor: BACKGROUND_COLOURS[color],
              brightness: Brightness.dark,
            ),
            routes: {
              ROUTES.hands: (context) => GamePage(),
              ROUTES.welcome: (context) => WelcomePage(),
              ROUTES.deadGames: (context) => GamesListPage(false),
              ROUTES.liveGames: (context) => GamesListPage(true),
              ROUTES.scoreSheet: (context) => ScoreSheetScreen(),
              ROUTES.hanFu: (context) => HanFuScreen(),
              ROUTES.help: (context) => HelpScreen(),
              ROUTES.selectPlayers: (context) => SelectPlayersScreen(),
              ROUTES.yaku: (context) => YakuScreen(),
              ROUTES.settings: (context) => SettingsScreen(),
              ROUTES.helpSettings: (context) =>
                  HelpScreen(page: ROUTES.helpSettings),
              ROUTES.chombo: (context) => WhoDidItScreen(
                    minPlayersSelected: 1,
                    maxPlayersSelected: 4,
                    whenDone: Scoring.calculateChombo,
                    displayStrings: {
                      'on': 'Chombo!',
                      'off': '-',
                      'prompt': 'Who chomboed?',
                    },
                  ),
              ROUTES.draw: (context) => WhoDidItScreen(
                    minPlayersSelected: 0,
                    maxPlayersSelected: 4,
                    preSelected: store.state.inRiichi,
                    whenDone: Scoring.calculateDrawScores,
                    displayStrings: {
                      'on': 'tenpai',
                      'off': 'noten',
                      'prompt': 'Who is in tenpai?',
                    },
                  ),
              ROUTES.multipleRon: (context) => WhoDidItScreen(
                    disableButton: store.state.result['losers'],
                    minPlayersSelected: 2,
                    maxPlayersSelected: 3,
                    whenDone: Scoring.multipleRons,
                    displayStrings: {
                      'on': 'Won!',
                      'off': 'Bystander',
                      'prompt': 'Who called ron?',
                    },
                  ),
              ROUTES.pao: (context) => WhoDidItScreen(
                    disableButton: store.state.result['winners'] is List
                        ? store.state.result['winners'].last
                        : store.state.result['winners'],
                    minPlayersSelected: 1,
                    maxPlayersSelected: 1,
                    whenDone: Scoring.calculatePao,
                    displayStrings: {
                      'on': 'Guilty!',
                      'off': 'Guilty?',
                      'prompt': 'Who is responsible? ',
                    },
                  ),
            },
          );
        },
      ),
    );
  }
}
