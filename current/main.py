import sys

import pygame

from menu import pause
from menu import start_screen

from house import House
from level import Level
from settings import *

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
level = Level(screen)
house = House(screen)
clock = pygame.time.Clock()
location = 'street'

start_screen()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                ded = False
                pause(ded)
            if pygame.key.get_pressed()[pygame.K_e] and level.can_enter_check() and location == 'street':
                location = 'house'
            elif pygame.key.get_pressed()[pygame.K_e] and house.can_out_check() and location == 'house':
                location = 'street'

    if location == 'street':
        screen.fill((153, 217, 234))
        level.run()
    elif location == 'house':
        screen.fill((0, 0, 0))
        house.run()

    pygame.display.update()
    clock.tick(60)
