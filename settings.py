#!/usr/bin/python
# -*- coding: utf-8 -*-

RESOLUTION = (1280, 720)
tile_size = 64

level_map = [
    '                            ',
    '                            ',
    '                            ',
    '               XXXXXX       ',
    '     XXXX        XXX        ',
    'XX         X                ',
    'XXXXX      X                ',
    '    XX     X                ',
    '         XXX   XX           ',
    '                      XX    ',
    'XXXXXXXXXXXXXXXXXXXXXXXX XXX',
]
level_entities = [{'type': 'player', 'pos': (0, 0)}]
level_data_test = {'level_map': level_map, 'level_entities': level_entities}
