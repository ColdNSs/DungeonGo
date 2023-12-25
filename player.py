#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg
from action import Action


class Player(pg.sprite.Sprite):
    def __init__(self, pos: tuple, level, dimension: tuple = (30, 60)):
        super().__init__()
        self.level = level
        self.dimension = dimension
        self.image = pg.Surface(self.dimension)
        self.image.fill('green')
        self.rect = self.image.get_rect(topleft=pos)
        self.is_player = True

        # player movement
        self.grav = 0.8
        self.jump_speed = -16
        self.walk_speed = 2
        self.sprint_speed = 4
        self.air_speed = 2
        self.accel = pg.Vector2(0, 0)
        self.decimal = pg.Vector2(0, 0)
        self.time_in_air = 0
        self.facing_right = True
        self.on_ground = True

        self.action = Action(executor=self, action_type='in_air', max_horizontal_speed=2, max_vertical_speed=16)
        self.down_inputs = []
        self.up_inputs = []
        self.hold_inputs = []

    def update_inputs(self, inputs: list):
        self.down_inputs = inputs[0]
        self.up_inputs = inputs[1]
        self.hold_inputs = inputs[2]

    def execute_action(self):
        self.action.update()

    def update(self, inputs: list):
        self.update_inputs(inputs)
        self.execute_action()
        # self.rect.topleft += pg.Vector2(1, 1)
