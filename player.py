#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg
from action import *


class Player(pg.sprite.Sprite):
    def __init__(self, pos: tuple, level, dimensions: tuple = (30, 60)):
        super().__init__()
        self.level = level
        self.dimensions = dimensions
        self.image = pg.Surface(self.dimensions)
        self.image.fill('green')
        self.rect = self.image.get_rect(topleft=pos)

        # player movement
        self.grav = 0.8
        self.jump_speed = -16
        self.walk_speed = 4
        self.sprint_speed = 8
        self.air_accel = 0.8
        self.air_fric = 0.4
        self.air_speed = 4
        self.max_vertical_speed = 20
        self.coyote_frames = 5
        self.accel = pg.Vector2(0, 0)
        self.veloc = pg.Vector2(0, 0)
        self.decimal = pg.Vector2(0, 0)

        self.facing_right = True
        self.on_ground = False

        self.action = InAirAction(executor=self, max_horizontal_speed=8, max_vertical_speed=self.max_vertical_speed)
        self.down_inputs = []
        self.up_inputs = []
        self.hold_inputs = []
        self.input_buffer = {'key': None, 'frame': -1, 'max_buffer_frames': 5}

    def update_inputs(self, inputs: list):
        self.down_inputs = inputs[0]
        self.up_inputs = inputs[1]
        self.hold_inputs = inputs[2]

        if pg.K_x in self.down_inputs:
            self.input_buffer['key'] = pg.K_x
            self.input_buffer['frame'] = self.input_buffer['max_buffer_frames']
        elif pg.K_z in self.down_inputs:
            self.input_buffer['key'] = pg.K_z
            self.input_buffer['frame'] = self.input_buffer['max_buffer_frames']

        if self.input_buffer['frame'] >= 0:
            self.input_buffer['frame'] -= 1

    def key_in_buffer(self, key: int):
        if self.input_buffer['key'] == key and self.input_buffer['frame'] >= 0:
            return True
        return False

    def update_on_ground(self):
        for sprite in self.level.tiles.sprites():
            if self.rect.bottom == sprite.rect.top and self.rect.left < sprite.rect.right and self.rect.right > sprite.rect.left:
                self.on_ground = True
                return True
        self.on_ground = False
        return False

    def update(self, inputs: list):
        self.update_inputs(inputs)
        self.action.update()
        # self.rect.topleft += pg.Vector2(1, 1)
