import sys
import pygame

from level import Level
from house import House
from settings import *

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
level = Level(screen)
house = House(screen)
clock = pygame.time.Clock()
location = 'house'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_e] and level.can_enter_check():
                location = 'house'

    screen.fill((153, 217, 234))
    if location == 'street':
        level.run()
    elif location == 'house':
        house.run()

    pygame.display.update()
    clock.tick(60)
