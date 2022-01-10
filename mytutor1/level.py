import pygame

from support import import_csv_layout, import_cut_graphics
from tiles import StaticTile, Crate
from settings import *


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.world_shift = -5

        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')

        grass_layout = import_csv_layout(level_data['grass'])
        self.grass_sprites = self.create_tile_group(grass_layout, 'grass')

        crates_layout = import_csv_layout(level_data['crates'])
        self.creates_sprites = self.create_tile_group(crates_layout, 'crates')

    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_ind, row in enumerate(layout):
            for col_ind, val in enumerate(row):
                if val != '-1':
                    x = col_ind * tile_size
                    y = row_ind * tile_size

                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphics('graphics/terrain/terrain_tiles.png')
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    elif type == 'grass':
                        grass_tile_list = import_cut_graphics('graphics/decoration/grass/grass.png')
                        tile_surface = grass_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    elif type == 'crates':
                        sprite = Crate(tile_size, x, y)

                    sprite_group.add(sprite)

        return sprite_group

    def run(self):
        self.terrain_sprites.update(self.world_shift)
        self.terrain_sprites.draw(self.display_surface)

        self.grass_sprites.update(self.world_shift)
        self.grass_sprites.draw(self.display_surface)

        self.creates_sprites.update(self.world_shift)
        self.creates_sprites.draw(self.display_surface)
