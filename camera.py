#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg
from settings import RESOLUTION


class CameraGroup(pg.sprite.Group):
    def __init__(self, player: pg.sprite.GroupSingle, display_surface: pg.Surface):
        super().__init__()
        self.player = player
        self.display_surface = display_surface

    def custom_draw(self):
        half_x = RESOLUTION[0] // 2
        half_y = RESOLUTION[1] // 2
        for sprite in self.sprites():
            c_pos = self.player.sprite.rect.center - pg.Vector2(half_x, half_y)
            draw_pos = sprite.rect.topleft - c_pos
            self.display_surface.blit(sprite.image, draw_pos)
