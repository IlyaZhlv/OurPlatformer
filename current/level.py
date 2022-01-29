import pygame
import pytmx

from player import Player
from zombies import Zombie1, Zombie2
from tiles import Tile
from settings import *


class Level:
    def __init__(self, display):
        self.display_surface = display
        self.world_shift = 0
        self.speed = 8
        self.world_tiles_offset = 349 * tile_size

        self.tmxdata = pytmx.load_pygame('../map/mainmap.tmx')
        self.player_sprite = self.create_player()

        self.zombie1_sprites = self.create_zombies('zombies')
        self.zombie2_sprites = self.create_zombies('zombies1')

        self.wall_sprites = self.create_walls()

        self.can_enter = False

    def can_enter_check(self):
        return self.can_enter

    def create_zombies(self, type):
        sprite = pygame.sprite.Group()

        for layer in self.tmxdata.layers:
            if layer.name == 'zombies' and type == 'zombies':
                for x, y, tile in layer.tiles():
                    zombie = Zombie1((x * tile_size - self.world_tiles_offset, y * tile_size + 15), '../map/zombies/zombie1')
                    sprite.add(zombie)

            elif layer.name == 'zombies1' and type == 'zombies1':
                for x, y, tile in layer.tiles():
                    zombie = Zombie2((x * tile_size - self.world_tiles_offset, y * tile_size + 15), '../map/zombies/zombie2')
                    sprite.add(zombie)

        return sprite

    def create_player(self):
        sprite = pygame.sprite.GroupSingle()

        for layer in self.tmxdata.layers:
            if layer.name == 'player':
                for x, y, tile in layer.tiles():
                    player = Player((x * tile_size - self.world_tiles_offset, y * tile_size), '../map/character/run/1.png')
                    sprite.add(player)
                    break

        return sprite

    def create_walls(self):
        sprite = pygame.sprite.Group()

        for layer in self.tmxdata.layers:
            if layer.name == 'walls':
                for x, y, tile in layer.tiles():
                    wall = Tile(tile_size, x * tile_size - self.world_tiles_offset, y * tile_size)
                    sprite.add(wall)

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

    def check_walls_collisions(self):
        for sprite in self.zombie1_sprites.sprites() + self.zombie2_sprites.sprites():
            if pygame.sprite.spritecollide(sprite, self.wall_sprites, False):
                sprite.reverse_speed()

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

            # elif layer.name == 'zombies':
            #     for x, y, tile in layer.tiles():
            #         test_image = pygame.image.load('../map/zombies/zombi1.png').convert_alpha()
            #         self.display_surface.blit(test_image, (x * tile_size - self.world_tiles_offset, y * tile_size))

            else:
                for x, y, tile in layer.tiles():
                    self.display_surface.blit(tile, (x * tile_size - self.world_tiles_offset, y * tile_size))

        self.player_sprite.draw(self.display_surface)

        self.wall_sprites.update(self.world_shift)

        self.zombie1_sprites.update(self.world_shift)
        self.zombie2_sprites.update(self.world_shift)
        self.check_walls_collisions()
        self.zombie1_sprites.draw(self.display_surface)
        self.zombie2_sprites.draw(self.display_surface)
