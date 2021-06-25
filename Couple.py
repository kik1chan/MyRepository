# -*- coding: utf-8 -*-
"""
couples
"""

import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
import random
from Settings import Settings


class Couple(Sprite):
    # the couple met on road

    def __init__(self, game_settings, screen):
        # init couple and set initial position
        super(Couple, self).__init__()
        self.screen = screen
        self.game_settings = game_settings
        self.couple_speed = game_settings.couple_speed_factor

        # load and show couple image and set its rect
        coupleFilename = ['bear_cat.png', 'fish.png', 'honey.png']
        rd = random.randint(0, 3)
        self.image = pygame.image.load(coupleFilename[rd])
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # initial position
        # randomly in the first, second or third line
        rand = random.randint(0, 3)
        if rand == 0:
            self.rect.x = 20
            self.rect.y = 20
        elif rand == 1:
            self.rect.x = 220
            self.rect.y = 20
        elif rand == 2:
            self.rect.x = 420
            self.rect.y = 20

        # store the specific location
        self.x = float(self.rect.x)

    def check_couple_edges(self, game_settings):
        # if couple is at the edges of screen, return True
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom:
            return True
        else:
            return False

    def blitme(self):
        # draw the couple at the specified location
        self.screen.blit(self.image, self.rect)

    def update(self):
        # couple move
        while self.check_couple_edges(game_settings):
            self.rect.y += self.couple_speed
            self.blitme()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    game_settings = Settings()
    pygame.display.set_caption("Couple test")

    couple = Couple(game_settings, screen)
    group = Group()
    group.add(couple)
    bgFilename = 'bg.jpg'
    bg = pygame.image.load(bgFilename)
    screen.blit(bg, [0, 0])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            exit()

        while True:
            group.update()
            group.draw(screen)
            pygame.display.flip()
