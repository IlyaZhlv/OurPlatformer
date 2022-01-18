import pygame

from tiles import StaticTile
from support import import_csv_layout, import_cut_graphics
from settings import *


class Level:
    def __init__(self, display, level_data):
        self.display_surface = display
        self.world_shift = -5
        self.world_tiles_offset = 349

        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_sprite_group(terrain_layout, 'terrain')

    def create_sprite_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_ind, row in enumerate(layout):
            for col_ind, val in enumerate(row):
                if val != '-1':
                    x = col_ind * tile_size - self.world_tiles_offset * tile_size
                    y = row_ind * tile_size

                    if type == 'terrain':
                        terrain_list_surface = import_cut_graphics('../map/еорм дорожи.png')
                        surface = terrain_list_surface[int(val)]
                        sprite = StaticTile(tile_size, x, y, surface)

                    sprite_group.add(sprite)

        return sprite_group

    def run(self):
        self.terrain_sprites.update(self.world_shift)
        self.terrain_sprites.draw(self.display_surface)
