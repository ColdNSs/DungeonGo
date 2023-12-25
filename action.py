#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg


class Action:
    def __init__(self, executor: pg.sprite.Sprite, action_type: str, max_horizontal_speed, max_vertical_speed):
        """
            Args:
                action_type (str): A string that should be one of these options:
                                  - 'idle'
                                  - 'walk'
                                  - 'sprint'
                                  - 'attack_1'
                                  - 'attack_2'
                                  - 'attack_3'
                                  - 'hurt'
                                  - 'dead'
                                  - 'in_air'
            """
        self.executor = executor
        self.type = action_type
        self.max_horizontal_speed = max_horizontal_speed
        self.max_vertical_speed = max_vertical_speed
        self.frame = 0
        self.hurtboxs = []
        self.hitboxs = []
        self.animation = None

    def animate(self):
        from player import Player
        if isinstance(self.executor, Player):
            print(str(self.frame))

    def update(self):
        self.frame += 1
        self.animate()
