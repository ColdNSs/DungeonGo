#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg
from tiles import Tile
from player import Player
from settings import tile_size
from camera import CameraGroup

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
    '     XXXXXXX   XX     XX    ',
    'XXXXXXXXXXXX   XXXXXXXXX XXX',
]
level_entities = [{'type': 'player', 'pos': (0, 0)}]
level_data_test = {'level_map': level_map, 'level_entities': level_entities}


class Level:
    def __init__(self, level_data: dict, surface: pg.Surface):
        self.display_surface = surface
        self.down_inputs = []
        self.up_inputs = []
        self.hold_inputs = []
        self.inputs = []

        self.tiles = pg.sprite.Group()
        self.player = pg.sprite.GroupSingle()

        for row_index, row in enumerate(level_data['level_map']):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    if (col_index + row_index) % 2 == 0:
                        tile = Tile('test_grey', (x, y), tile_size)
                    else:
                        tile = Tile('test_white', (x, y), tile_size)
                    self.tiles.add(tile)

        for entity in level_data['level_entities']:
            if entity['type'] == 'player':
                player_sprite = Player(entity['pos'], self)
                self.player.add(player_sprite)

        self.camera = CameraGroup(player=self.player, display_surface=self.display_surface)

    def update_inputs(self, events: list[pg.event.Event]):
        # clear inputs
        self.down_inputs = []
        self.up_inputs = []
        # self.hold_inputs = []

        # update tap inputs
        for event in events:
            if event.type == pg.KEYDOWN:
                self.down_inputs.append(event.key)
            if event.type == pg.KEYUP:
                self.up_inputs.append(event.key)

        # update hold inputs
        keys = pg.key.get_pressed()
        self.hold_inputs = keys
        self.inputs = [self.down_inputs, self.up_inputs, self.hold_inputs]

    def run(self, events: list[pg.event.Event]):
        # update inputs
        self.update_inputs(events)

        # tiles update
        self.tiles.update()

        # player update
        self.player.update(self.inputs)

        # draw
        self.camera.add(self.tiles)
        self.camera.add(self.player)
        self.camera.custom_draw()
