import sys
import pygame

from level import Level
from gamedata import level_0
from settings import *

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
level = Level(screen, level_0)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.init()
            sys.exit()

    screen.fill('black')
    level.run()
    pygame.display.update()
    clock.tick(60)
