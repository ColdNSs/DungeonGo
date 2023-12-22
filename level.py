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
    def __init__(self, level_data, surface):
        self.display_surface = surface

        self.tiles = pg.sprite.Group()
        self.player = pg.sprite.GroupSingle()

        for row_index, row in enumerate(level_data['level_map']):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Tile('test_grey', (x, y), tile_size)
                    self.tiles.add(tile)

        for entity in level_data['level_entities']:
            if entity['type'] == 'player':
                player_sprite = Player(entity['pos'], self)
                self.player.add(player_sprite)

        self.camera = CameraGroup(player=self.player, display_surface=self.display_surface)

    def run(self):
        # tiles update
        self.tiles.update()
        # self.tiles.draw(self.display_surface)

        # player update
        self.player.update()
        # self.player.draw(self.display_surface)

        # draw
        self.camera.add(self.tiles)
        self.camera.add(self.player)
        self.camera.custom_draw()
