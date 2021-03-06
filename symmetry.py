# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:18:31 2019

@author: Andrew
"""

PANTHEON_RIICHI = 33;
PANTHEON_PINFU = 8;
PANTHEON_CHITOITSU = 31;
PANTHEON_TSUMO = 36;
PAO_FLAG = 8888;

fluttermap = {
  PANTHEON_RIICHI: [],
  -3: [6, 7, 19, 20, 21, 22, 26, 29, 30, 32, 39, 40, 43, PAO_FLAG,],
  -2: [6, 7, 19, 20, 21, 22, 26, 29, 30, 32, 39, 40, 43, PAO_FLAG,],
  -1: [6, 7, 19, 20, 21, 22, 26, 29, 30, 32, 39, 40, PAO_FLAG,],
  1: [6, 7, PANTHEON_PINFU, 9, 10, 11, 12, 19, 20, 21, 22, 24, 25, 26, 29, 30, PANTHEON_CHITOITSU, 32, PANTHEON_TSUMO, 39, 40, 43, PAO_FLAG,],
  2: [6, 7, PANTHEON_PINFU, 9, 10, 11, 12, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 32, PANTHEON_TSUMO, 39, 40, 43, PAO_FLAG,],
  3: [6, 7, PANTHEON_PINFU, 9, 10, 11, 12, 19, 20, 21, 22, 26, 29, 30, PANTHEON_CHITOITSU, 32, 39, 40, 43, PAO_FLAG,],
  4: [6, 7, PANTHEON_PINFU, 9, 10, 11, 12, 18, 19, 20, 21, 22, 26, 27, 28, 29, 30, PANTHEON_CHITOITSU, 32, 39, 40, 43, PAO_FLAG,],
  5: [6, 7, PANTHEON_PINFU, 9, 10, 11, 12, 19, 20, 21, 22, 26, 29, 30, PANTHEON_CHITOITSU, 32, 39, 40, 43, PAO_FLAG,],
  6: [-11, -3, -2, -1, 1, 2, 3, 4, 5, 7, PANTHEON_PINFU, 9, 10, 11, 12, 13, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, PANTHEON_CHITOITSU, 32, 34, 35, 37, 38, 39, 40, 41, 42, 43, PAO_FLAG,],
  7: [-11, -3, -2, -1, 1, 2, 3, 4, 5, 6, PANTHEON_PINFU, 9, 10, 11, 12, 13, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, PANTHEON_CHITOITSU, 32, 34, 35, 37, 38, 39, 40, 41, 42, 43, PAO_FLAG,],
  PANTHEON_PINFU: [1, 2, 3, 4, 5, 6, 7, 13, 18, 19, 20, 21, 22, 26, 29, 30, PANTHEON_CHITOITSU, 32, 38, 39, 40, 43, PAO_FLAG,],
  9: [1, 2, 3, 4, 5, 6, 7, 10, 19, 20, 21, 22, 26, 29, 30, PANTHEON_CHITOITSU, 32, 39, 40, 43, PAO_FLAG,],
  10: [1, 2, 3, 4, 5, 6, 7, 9, 11, 12, 13, 18, 19, 20, 21, 22, 26, 29, 30, PANTHEON_CHITOITSU, 32, 38, 39, 40, 43, PAO_FLAG,],
  11: [1, 2, 3, 4, 5, 6, 7, 10, 12, 18, 18, 19, 20, 21, 22, 26, 27, 28, 29, 30, PANTHEON_CHITOITSU, 32, 39, 40, 43, PAO_FLAG,],
  12: [1, 2, 3, 4, 5, 6, 7, 10, 11, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29, 30, PANTHEON_CHITOITSU, 32, 39, 40, 43, PAO_FLAG,],
  13: [6, 7, PANTHEON_PINFU, 10, 19, 20, 21, 22, 23, 25, 26, 28, 29, 30, PANTHEON_CHITOITSU, 32, 39, 40, 43, PAO_FLAG,],
  18: [4, 6, 7, PANTHEON_PINFU, 10, 11, 12, 19, 20, 21, 22, 23, 25, 26, 28, 28, 29, 30, PANTHEON_CHITOITSU, 32, 39, 40, 43, PAO_FLAG,],
  19: [-11, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, PANTHEON_PINFU, 9, 10, 11, 12, 13, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, PANTHEON_CHITOITSU, 32, 34, 35, 37, 38, 39, 40, 41, 42, 43,],
  20: [-11, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, PANTHEON_PINFU, 9, 10, 11, 12, 13, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, PANTHEON_CHITOITSU, 32, 34, 35, 37, 38, 39, 40, 41, 42, 43,],
  21: [-11, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, PANTHEON_PINFU, 9, 10, 11, 12, 13, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, PANTHEON_CHITOITSU, 32, 34, 35, 37, 38, 39, 40, 41, 42, 43, PAO_FLAG,],
  22: [-11, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, PANTHEON_PINFU, 9, 10, 11, 12, 13, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30, PANTHEON_CHITOITSU, 32, 34, 35, 37, 38, 39, 40, 41, 42, 43, PAO_FLAG,],
  23: [2, 6, 7, 12, 13, 18, 19, 20, 21, 22, 24, 25, 26, 27, 29, 30, 32, 39, 40, 43, PAO_FLAG,],
  24: [1, 2, 6, 7, 12, 19, 20, 21, 22, 23, 25, 26, 28, 29, 30, PANTHEON_CHITOITSU, 32, 39, 40, 43, PAO_FLAG,],
  25: [1, 2, 6, 7, 12, 13, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, PANTHEON_CHITOITSU, 32, 39, 40, 43, PAO_FLAG,],
  26: [-11, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, PANTHEON_PINFU, 9, 10, 11, 12, 13, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, PANTHEON_CHITOITSU, 32, 34, 35, 37, 38, 39, 40, 41, 42, 43, PAO_FLAG,],
  27: [4, 6, 7, 11, 19, 20, 21, 22, 23, 25, 26, 28, 29, 30, 32, 39, 40, 43, PAO_FLAG,],
  28: [2, 4, 6, 7, 11, 13, 18, 19, 20, 21, 22, 24, 25, 26, 27, 29, 30, 32, 39, 40, 43, PAO_FLAG,],
  29: [-11, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, PANTHEON_PINFU, 9, 10, 11, 12, 13, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, PANTHEON_CHITOITSU, 32, 34, 35, 37, 38, 39, 40, 41, 42, 43, PAO_FLAG,],
  30: [-11, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, PANTHEON_PINFU, 9, 10, 11, 12, 13, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, PANTHEON_CHITOITSU, 32, 34, 35, 37, 38, 39, 40, 41, 42, 43, PAO_FLAG,],
  PANTHEON_CHITOITSU: [1, 3, 4, 5, 6, 7, PANTHEON_PINFU, 9, 10, 11, 12, 13, 18, 19, 20, 21, 22, 24, 25, 26, 29, 30, 32, 38, 39, 40, 43, PAO_FLAG,],
  32: [-11, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, PANTHEON_PINFU, 9, 10, 11, 12, 13, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, PANTHEON_CHITOITSU, 34, 35, 37, 38, 39, 40, 41, 42, 43, PAO_FLAG,],
  34: [6, 7, 19, 20, 21, 22, 26, 29, 30, 32, 39, 40, 43, PAO_FLAG,],
  35: [6, 7, 19, 20, 21, 22, 26, 29, 30, 32, 39, 40, 43, PAO_FLAG,],
  PANTHEON_TSUMO: [1, 2, 41, 43,],
  37: [6, 7, 19, 20, 21, 22, 26, 29, 30, 32, 38, 39, 40, 41, 42, 43, PAO_FLAG,],
  38: [6, 7, PANTHEON_PINFU, 10, 19, 20, 21, 22, 26, 29, 30, PANTHEON_CHITOITSU, 32, 37, 37, 37, 39, 40, 41, 42, 43, PAO_FLAG,],
  39: [-11, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, PANTHEON_PINFU, 9, 10, 11, 12, 13, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, PANTHEON_CHITOITSU, 32, 34, 35, 37, 38, 40, 41, 42, 43, PAO_FLAG,],
  40: [-11, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, PANTHEON_PINFU, 9, 10, 11, 12, 13, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, PANTHEON_CHITOITSU, 32, 34, 35, 37, 38, 39, 41, 42, 43, PAO_FLAG,],
  41: [6, 7, 19, 20, 21, 22, 26, 29, 30, 32, PANTHEON_TSUMO, 37, 38, 39, 40, 42, 43, PAO_FLAG,],
  42: [6, 7, 19, 20, 21, 22, 26, 29, 30, 32, 37, 38, 39, 40, 41, 43, PAO_FLAG,],
  43: [-11, -3, -2, 1, 2, 3, 4, 5, 6, 7, PANTHEON_PINFU, 9, 10, 11, 12, 13, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, PANTHEON_CHITOITSU, 32, 34, 35, PANTHEON_TSUMO, 37, 38, 39, 40, 41, 42, PAO_FLAG,],
  PAO_FLAG: [-11, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, PANTHEON_PINFU, 9, 10, 11, 12, 13, 18, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, PANTHEON_CHITOITSU, 32, 34, 35, 37, 38, 39, 40, 41, 42, 43,],
}

errors = False
for (key, val) in fluttermap.items():
    for key2 in val:
        if key2 in fluttermap and key not in fluttermap[key2]:
            errors = True
            print('%d, %d ERROR' % (key, key2))

replacers = {
33: 'PANTHEON_RIICHI',
8: 'PANTHEON_PINFU',
31: 'PANTHEON_CHITOITSU',
36: 'PANTHEON_TSUMO',
8888: 'PAO_FLAG',
}

if not errors:
    for key in sorted(fluttermap):
        val = fluttermap[key]
        val.sort()
        vals = '['
        for oneval in val:
            vals += ' %d,' % oneval
        vals += '],'
        for (num, string) in replacers.items():
            vals = vals.replace(' %d,' % num, ' '+string+',');
        keys = replacers[key] if key in replacers else ('%d' % key)
        print('%s: %s' % (keys, vals.replace(', ',',')))
    print('\n\nNo errors!')