# -*- coding: utf-8 -*-
"""
game_functions
"""

import sys

import pygame
import random

from Couple import Couple


def check_keydown_events(event, role):
    # response when keydown
    if event.key == pygame.K_RIGHT:
        role.moving_right = True
    elif event.key == pygame.K_LEFT:
        role.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, role):
    # response when keydown
    if event.key == pygame.K_RIGHT:
        role.moving_right = False
    elif event.key == pygame.K_LEFT:
        role.moving_left = False


def update_screen(game_settings, screen, role, couples):
    # load and show the background image
    imgFileName = 'bg.jpg'
    imgRect = pygame.image.load(imgFileName)
    screen.blit(imgRect, [0, 0])
    # show the role
    role.blitme()
    # show the couples
    # couple.biltme(screen)
    couples.draw(screen)
    # diaplay
    pygame.display.flip()


def get_number_couples_x(game_settings, round=1):
    # culculate the number of couples
    rand = random.randint(3, 8)
    return 2 * (round + rand)


def create_couple(game_settings, screen, couples, couple_number):
    # create current couple
    couple = Couple(game_settings, screen)
    couples.add(couple)


def create_couples(game_settings, screen, couples):
    # create couples
    number_couples_x = random.randint(10, 12)

    # create couples according to number_couples_x
    for couple_number in range(number_couples_x):
        create_couple(game_settings, screen, couples, couple_number)


def update_couples(game_settings, role, couples):
    # update couples location
    check_couple_edges(game_settings, couples)
    couples.update()

    # check the collision
    if pygame.sprite.spritecollideany(role, couples):
        print("you lose!")


def update_role(role, couples):
    # update couples if they had effective collision by role

    # check whether they had collision
    collisions = []
    for couple in couples:
        collisions.append(pygame.sprite.collide_rect(role, couple))
