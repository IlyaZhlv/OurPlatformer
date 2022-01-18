import pygame
import pytmx

from player import Player
from settings import *


class Level:
    def __init__(self, display):
        self.display_surface = display
        self.world_shift = 0
        self.world_tiles_offset = 349 * tile_size

        # terrain_layout = import_csv_layout(level_data['terrain'])
        # self.terrain_sprites = self.create_sprite_group(terrain_layout, 'terrain')

        self.tmxdata = pytmx.load_pygame('../map/mainmap.tmx')
        self.player_sprite = self.create_player()

    def create_player(self):
        sprite = pygame.sprite.GroupSingle()

        for layer in self.tmxdata.layers:
            if layer.name == 'player':
                for x, y, tile in layer.tiles():
                    player = Player((x * tile_size - self.world_tiles_offset, y * tile_size), '../map/character/run/1.png')
                    sprite.add(player)
                    break

        return sprite

    def scroll_x(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.world_tiles_offset += 8

        elif keys[pygame.K_a]:
            self.world_tiles_offset += -8

    def run(self):
        self.scroll_x()
        for layer in self.tmxdata.visible_layers:
            for x, y, tile in layer.tiles():
                self.display_surface.blit(tile, (x * tile_size - self.world_tiles_offset, y * tile_size))

        self.player_sprite.update()
        self.player_sprite.draw(self.display_surface)
        # self.terrain_sprites.update(self.world_shift)
        # self.terrain_sprites.draw(self.display_surface)
