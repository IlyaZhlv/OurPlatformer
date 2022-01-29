import csv
import pygame
from os import walk

from settings import *


def import_csv_layout(path):
    layout_list = []
    with open(path) as map:
        reader = csv.reader(map, delimiter=',')
        for row in reader:
            layout_list.append(list(row))
        return layout_list


def import_cut_graphics(path):
    surface = pygame.image.load(path)
    x_num = surface.get_size()[0] // 40
    y_num = surface.get_size()[1] // 90

    tiles_list = []
    for col in range(x_num):
        for row in range(y_num):
            x = col * tile_size
            y = row * tile_size
            new_surf = pygame.Surface((40, 90))
            new_surf.blit(surface, (0, 0), pygame.Rect(x, y, 40, 90))
            tiles_list.append(pygame.Rect(x, y, 40, 90))

    return tiles_list


def import_folder(path):
    surface_list = []

    for _, __, image_files in walk(path):
        for image in image_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list
