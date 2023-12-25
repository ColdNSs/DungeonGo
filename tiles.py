#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg

test_grey = {'color': 'grey', 'surf': None}
test_white = {'color': 'white', 'surf': None}
marisad = {'color': 'green', 'surf': pg.image.load('assets/window/icon.png')}

tiles_dic = {'test_grey': test_grey, 'test_white': test_white, 'marisad': marisad}


class Tile(pg.sprite.Sprite):
    def __init__(self, mat: str, pos: tuple = (0, 0), size: int = 100):
        super().__init__()
        self.image = pg.Surface((size, size))
        self.rect = self.image.get_rect(topleft=pos)

        self.mat = mat
        self.image.fill(tiles_dic[self.mat]['color'])
        if tiles_dic[self.mat]['surf']:
            self.image.blit(tiles_dic[self.mat]['surf'], (0, 0))

    def update(self):
        pass
