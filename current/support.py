import csv
import pygame

from settings import *


def import_csv_layout(path):
    layout_list = []
    with open(path) as map:
        reader = csv.reader(map, delimiter=',')
        for row in reader:
            layout_list.append(list(row))
        return layout_list


def import_cut_graphics(path):
    surface = pygame.image.load(path).convert_alpha()
    x_num = surface.get_size()[0] // tile_size
    y_num = surface.get_size()[1] // tile_size

    tiles_list = []
    for row in range(x_num):
        for col in range(y_num):
            x = col * tile_size
            y = row * tile_size
            new_surf = pygame.Surface((tile_size, tile_size))
            new_surf.blit(surface, (0, 0), pygame.Rect(x, y, tile_size, tile_size))
            tiles_list.append(new_surf)

    return tiles_list
