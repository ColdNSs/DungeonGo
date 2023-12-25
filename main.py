#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg
from sys import exit
from settings import *
from level import Level

if __name__ == '__main__':
    pg.init()

    # display window
    screen = pg.display.set_mode(RESOLUTION)
    pg.display.set_caption('DungeonGo')
    icon_image = pg.image.load('assets/window/icon.png')
    pg.display.set_icon(icon_image)

    # clock
    clock = pg.time.Clock()

    # levels
    level = Level(level_data_test, screen)

    # main loop
    while True:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                exit()

        # bg
        screen.fill('black')

        # level
        level.run(events)

        # update
        pg.display.update()
        clock.tick(60)
