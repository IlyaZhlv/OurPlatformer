import pygame
import pytmx

from player import Player
from settings import *


class Level:
    def __init__(self, display):
        self.display_surface = display
        self.world_shift = 0
        self.speed = 8
        self.world_tiles_offset = 349 * tile_size

        self.tmxdata = pytmx.load_pygame('../map/mainmap.tmx')
        self.player_sprite = self.create_player()

        self.can_enter = False

    def can_enter_check(self):
        return self.can_enter

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

        if keys[pygame.K_d] and not keys[pygame.K_a]:
            self.world_shift = self.speed

        elif keys[pygame.K_a] and not keys[pygame.K_d]:
            self.world_shift = -self.speed

        else:
            self.world_shift = 0

        self.world_tiles_offset += self.world_shift

    def run(self):
        self.scroll_x()
        self.player_sprite.update()

        for layer in self.tmxdata.visible_layers:
            if layer.name == 'terrain':
                for x, y, tile in layer.tiles():
                    if pygame.Rect(x * tile_size - self.world_tiles_offset, y * tile_size, tile_size, tile_size).colliderect(self.player_sprite.sprite.rect):
                        self.player_sprite.sprite.vertical_collisions(y * tile_size)

                    self.display_surface.blit(tile, (x * tile_size - self.world_tiles_offset, y * tile_size))

            elif layer.name == 'enter':
                for x, y, tile in layer.tiles():
                    if tile_size * 14 <= x * tile_size - self.world_tiles_offset <= tile_size * 22:
                        self.can_enter = True
                    else:
                        self.can_enter = False

            else:
                for x, y, tile in layer.tiles():
                    self.display_surface.blit(tile, (x * tile_size - self.world_tiles_offset, y * tile_size))

        self.player_sprite.draw(self.display_surface)
