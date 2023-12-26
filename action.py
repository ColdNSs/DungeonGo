#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg
from typing import TYPE_CHECKING, Union
from math import copysign

if TYPE_CHECKING:
    from player import Player

"""
  - 'on_ground'
  - 'attack_1'
  - 'attack_2'
  - 'attack_3'
  - 'hurt'
  - 'dead'
  - 'in_air'
            """


class Action:
    def __init__(self, executor):
        self.executor = executor
        self.frame = -1
        self.hurtboxs = []
        self.hitboxs = []
        self.animation = None
        self.pause = 0
        self.type = 'action'

    def calc_move(self):
        pass

    def add_to_decimal(self):
        self.executor.decimal += self.executor.veloc

        move_x = int(self.executor.decimal.x)
        self.executor.decimal.x -= move_x
        move_y = int(self.executor.decimal.y)
        self.executor.decimal.y -= move_y

        self.move((move_x, move_y))

    def move(self, vector: tuple):
        executor = self.executor

        # vertical movement
        executor.rect.y += vector[1]
        for sprite in executor.level.tiles.sprites():
            if sprite.rect.colliderect(executor.rect):
                if vector[1] < 0:
                    executor.rect.top = sprite.rect.bottom
                else:
                    executor.rect.bottom = sprite.rect.top
                executor.accel.y = 0
                executor.veloc.y = 0
                executor.decimal.y = 0

        # horizontal movement
        executor.rect.x += vector[0]
        for sprite in executor.level.tiles.sprites():
            if sprite.rect.colliderect(executor.rect):
                if vector[0] < 0:
                    executor.rect.left = sprite.rect.right
                else:
                    executor.rect.right = sprite.rect.left
                executor.accel.x = 0
                executor.veloc.x = 0
                executor.decimal.x = 0

    def update_hurtboxs(self):
        pass

    def update_hitboxs(self):
        pass

    def update_action(self):
        pass

    def animate(self):
        pass

    def update(self):
        if self.pause > 0:
            self.pause -= 1
            self.update_action()
        else:
            self.frame += 1
            self.calc_move()
            self.update_hurtboxs()
            self.update_hitboxs()
            self.update_action()
            self.animate()


class InAirAction(Action):
    def __init__(self, executor, max_horizontal_speed, max_vertical_speed):
        super().__init__(executor)
        self.type = 'in_air'
        self.max_horizontal_speed = max_horizontal_speed
        self.max_vertical_speed = max_vertical_speed

        if TYPE_CHECKING:
            self.executor = executor

    def calc_move(self):
        # horizontal accel
        if self.executor.hold_inputs[pg.K_LEFT] and not self.executor.hold_inputs[pg.K_RIGHT]:
            self.executor.accel.x = - self.executor.air_accel
        elif not self.executor.hold_inputs[pg.K_LEFT] and self.executor.hold_inputs[pg.K_RIGHT]:
            self.executor.accel.x = self.executor.air_accel
        else:
            if abs(self.executor.veloc.x) <= self.executor.air_fric:
                self.executor.accel.x = 0
                self.executor.veloc.x = 0
            else:
                self.executor.accel.x = 0 - copysign(self.executor.air_fric, self.executor.veloc.x)

        # vertical accel
        if self.executor.veloc.y > 5:
            self.executor.grav = 1.0
        else:
            self.executor.grav = 0.8
        self.executor.accel.y = self.executor.grav

        # add to veloc
        self.executor.veloc += self.executor.accel
        if abs(self.executor.veloc.x) > self.max_horizontal_speed:
            self.executor.veloc.x = copysign(self.max_horizontal_speed, self.executor.veloc.x)
        if abs(self.executor.veloc.y) > self.max_vertical_speed:
            self.executor.veloc.y = copysign(self.max_vertical_speed, self.executor.veloc.y)

        # coyote jump
        if self.executor.key_in_buffer(pg.K_x) and self.executor.veloc.y >= 0 and self.frame < 4:
            self.executor.veloc.y = self.executor.jump_speed
            self.executor.input_buffer['frame'] = -1

        # add to decimal
        self.add_to_decimal()

    def update_action(self):
        super().update_action()
        self.executor.update_on_ground()
        if self.executor.on_ground:
            self.executor.action = OnGroundAction(self.executor)


class OnGroundAction(Action):
    def __init__(self, executor):
        super().__init__(executor)

    def calc_move(self):
        # horizontal veloc
        self.executor.veloc.x = 0
        if self.executor.hold_inputs[pg.K_LEFT] and not self.executor.hold_inputs[pg.K_RIGHT]:
            self.executor.veloc.x = - self.executor.walk_speed
            if self.executor.hold_inputs[pg.K_LSHIFT]:
                self.executor.veloc.x = - self.executor.sprint_speed
        elif not self.executor.hold_inputs[pg.K_LEFT] and self.executor.hold_inputs[pg.K_RIGHT]:
            self.executor.veloc.x = self.executor.walk_speed
            if self.executor.hold_inputs[pg.K_LSHIFT]:
                self.executor.veloc.x = self.executor.sprint_speed

        # vertical veloc
        self.executor.veloc.y = 0
        if self.executor.key_in_buffer(pg.K_x):
            self.executor.veloc.y = self.executor.jump_speed

        # add to decimal
        self.add_to_decimal()

    def update_action(self):
        super().update_action()
        self.executor.update_on_ground()
        if not self.executor.on_ground:
            self.executor.action = InAirAction(self.executor, max_horizontal_speed=max(4, abs(self.executor.veloc.x)), max_vertical_speed=self.executor.max_vertical_speed)
