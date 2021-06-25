# -*- coding: utf-8 -*-
"""
Settings
"""


from pygame.color import THECOLORS


class Settings():

    # init
    def __init__(self):
        # screen
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = THECOLORS['lemonchiffon']

        # speed
        self.role_speed_factor = 1.5
        self.couple_speed_factor = 10
