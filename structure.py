# -*- coding: utf-8 -*-
"""
Animal Run

structure
"""


import pygame

from pygame.sprite import Group
from Settings import Settings
from Role import Role
# from Couple import Couple
import game_functions as gf


def run_game():
    # init
    pygame.init()
    game_settings = Settings()
    width = game_settings.screen_width
    height = game_settings.screen_height
    screen = pygame.display.set_mode((width, height))

    # title
    pygame.display.set_caption('Animal Run')

    # create a role
    role = Role(game_settings, screen)

    # create a group of couple
    couples = Group()
    gf.create_couples(game_settings, screen, couples)

    # repeating loop
    while True:
        coverFilename = 'cover.png'
        cover = pygame.image.load(coverFilename)
        screen.blit(cover, [0, 0])

        '''
        gf.check_keydown_events()
        role.update()
        gf.update_couples(game_settings, role, couples)
        gf.update_screen(game_settings, screen, role)
        '''


if __name__ == '__main__':
    run_game()
