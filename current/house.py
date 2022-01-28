import pygame
import pytmx

from player import Player
from settings import *


class House:
    def __init__(self, display):
        self.display_surface = display
        self.player_shift = 0
        self.speed = 5
        self.world_tiles_offset_x = -90
        self.world_tiles_offset_y = vertical_tile_number // 2 * tile_size - tile_size * 3

        self.tmxdata = pytmx.load_pygame('../map/home.tmx')
        self.player_sprite = self.create_player()

        self.can_out = False
        self.is_colliding = False

    def can_out_check(self):
        return self.can_out

    def create_player(self):
        sprite = pygame.sprite.GroupSingle()

        for layer in self.tmxdata.layers:
            if layer.name == 'player':
                for x, y, tile in layer.tiles():
                    player = Player((x * tile_size - self.world_tiles_offset_x, y * tile_size + self.world_tiles_offset_y), '../map/character/run/1.png')
                    sprite.add(player)
                    break

        return sprite

    def scroll_x(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] and not keys[pygame.K_a] and not self.is_colliding:
            self.player_shift = self.speed

        elif keys[pygame.K_a] and not keys[pygame.K_d] and not self.is_colliding:
            self.player_shift = -self.speed

        else:
            self.player_shift = 0

        self.player_sprite.sprite.rect.x += self.player_shift

    def run(self):
        self.scroll_x()
        self.player_sprite.update()
        self.is_colliding = False

        for layer in self.tmxdata.visible_layers:
            if layer.name == 'не прозрачно':
                for x, y, tile in layer.tiles():
                    if pygame.Rect(x * tile_size - self.world_tiles_offset_x, y * tile_size + self.world_tiles_offset_y, tile_size, tile_size).colliderect(self.player_sprite.sprite.rect):
                        self.player_sprite.sprite.vertical_collisions(y * tile_size + self.world_tiles_offset_y)

                    self.display_surface.blit(tile, (x * tile_size - self.world_tiles_offset_x, y * tile_size + self.world_tiles_offset_y))

            elif layer.name == 'out':
                for x, y, tile in layer.tiles():
                    # if tile_size * 14 <= x * tile_size - self.world_tiles_offset_x <= tile_size * 22:
                    #     self.can_enter = True
                    # else:
                    #     self.can_enter = False
                    if self.player_sprite.sprite.rect.x - (x * tile_size - self.world_tiles_offset_x) < tile_size * 2:
                        self.can_out = True
                    else:
                        self.can_out = False

            elif layer.name == 'walls':
                for x, y, tile in layer.tiles():
                    if pygame.Rect(x * tile_size - self.world_tiles_offset_x, y * tile_size + self.world_tiles_offset_y, tile_size, tile_size).colliderect(self.player_sprite.sprite.rect):
                        if self.player_shift < 0:
                            self.is_colliding = True
                            self.player_sprite.sprite.rect.left = x * tile_size + tile_size - self.world_tiles_offset_x

                        elif self.player_shift > 0:
                            self.is_colliding = True
                            self.player_sprite.sprite.rect.right = x * tile_size - self.world_tiles_offset_x

                    self.display_surface.blit(tile, (x * tile_size - self.world_tiles_offset_x, y * tile_size + self.world_tiles_offset_y))

            else:
                for x, y, tile in layer.tiles():
                    self.display_surface.blit(tile, (x * tile_size - self.world_tiles_offset_x, y * tile_size + self.world_tiles_offset_y))

        self.player_sprite.draw(self.display_surface)
