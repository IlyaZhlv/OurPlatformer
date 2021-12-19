import pygame
from settings import tile_size

from tiles import Tile


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == 'X':
                    tile = Tile((col_index * tile_size, row_index * tile_size), tile_size)
                    self.tiles.add(tile)

    def run(self):
        self.tiles.draw(self.display_surface)