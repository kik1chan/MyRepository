# -*- coding: utf-8 -*-
"""
Role
"""

import pygame
from pygame.sprite import Sprite
from Settings import Settings


class Role(Sprite):

    def __init__(self, game_settings, screen):
        # init
        super(Role, self).__init__()
        self.screen = screen
        self.game_settings = game_settings
        self.image = None
        self.master_image = None
        self.rect = None
        self.topleft = 0, 0
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0

        # load the role image and get the size of image
        self.image = pygame.image.load('bear.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put the role in the central bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # type of center: int -> float
        self.center = float(self.rect.centerx)

        # move sign
        self.moving_right = False
        self.moving_left = False

    def load(self, filename, width, height, columns):
        # load the sequence images of sprite
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = 220, 420, width, height
        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate=100):
        # update frame
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = (frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame
        '''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += 200
        if self.moving_left and self.rect.left > 0:
            self.centerx -= 200

        # update rect according to self.center
        self.rect.centerx = self.center
        '''

    def blitme(self):
        # draw the role at the specified location
        self.screen.blit(self.image, self.rect)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    game_settings = Settings()
    pygame.display.set_caption("Role test")
    font = pygame.font.Font(None, 18)
    framerate = pygame.time.Clock()

    bear = Role(game_settings, screen)
    bear.load("bear.png", 160, 160, 2)
    group = pygame.sprite.Group()
    group.add(bear)

    while True:
        # set time
        framerate.tick(30)
        ticks = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            exit()

        bgFilename = 'bg.jpg'
        bg = pygame.image.load(bgFilename)
        screen.blit(bg, [0, 0])

        group.update(ticks)
        group.draw(screen)
        pygame.display.update()
