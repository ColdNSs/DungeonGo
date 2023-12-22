#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, pos: tuple, level, dimension: tuple = (30, 60)):
        super().__init__()
        self.level = level
        self.dimension = dimension
        self.image = pg.Surface(self.dimension)
        self.image.fill('green')
        self.rect = self.image.get_rect(topleft=pos)

        # player movement
        self.decimal = pg.Vector2(0, 0)
        self.grav = 0.8
        self.jump_speed = -16
        self.time_in_air = 0
        self.accel = pg.Vector2(0, 0)
        self.facing_right = True

    def update(self):
        self.rect.topleft += pg.Vector2(1, 1)
