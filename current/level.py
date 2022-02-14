import sys

import pygame
import pytmx

from player import Player
from zombies import Zombie1, Zombie2, Zombie3, Zombie4
from tiles import Tile
from display import Health, Task, Ban
from settings import *


class Level:
    def __init__(self, display):
        self.display_surface = display
        self.world_shift = 0
        self.speed = 8
        self.world_tiles_offset = 354 * tile_size
        self.zombie_count = 0
        self.player_health = 100
        self.ban_count = 0

        self.tmxdata = pytmx.load_pygame('../map/mainmap.tmx')
        self.player_sprite = self.create_player()

        self.zombie1_sprites = self.create_zombies('zombies1')
        self.zombie2_sprites = self.create_zombies('zombies2')
        self.zombie3_sprites = self.create_zombies('zombies3')
        self.zombie4_sprites = self.create_zombies('zombies4')

        self.wall_sprites = self.create_walls()

        self.can_enter = False

        self.health = Health(self.display_surface)
        self.task = Task(self.display_surface)
        self.ban = Ban(self.display_surface)

    def can_enter_check(self):
        return self.can_enter

    def create_zombies(self, type):
        sprite = pygame.sprite.Group()

        for layer in self.tmxdata.layers:
            if layer.name == 'zombies1' and type == 'zombies1':
                for x, y, tile in layer.tiles():
                    zombie = Zombie1((x * tile_size - self.world_tiles_offset, y * tile_size + 15), '../map/zombies/zombie1')
                    sprite.add(zombie)
                    self.zombie_count += 1

            elif layer.name == 'zombies2' and type == 'zombies2':
                for x, y, tile in layer.tiles():
                    zombie = Zombie2((x * tile_size - self.world_tiles_offset, y * tile_size + 15), '../map/zombies/zombie2')
                    sprite.add(zombie)
                    self.zombie_count += 1

            elif layer.name == 'zombies3' and type == 'zombies3':
                for x, y, tile in layer.tiles():
                    zombie = Zombie3((x * tile_size - self.world_tiles_offset, y * tile_size + 15), '../map/zombies/zombie3')
                    sprite.add(zombie)
                    self.zombie_count += 1

            elif layer.name == 'zombies4' and type == 'zombies4':
                for x, y, tile in layer.tiles():
                    zombie = Zombie4((x * tile_size - self.world_tiles_offset, y * tile_size + 15), '../map/zombies/zombie4')
                    sprite.add(zombie)
                    self.zombie_count += 1

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

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_r] and self.ban_count == 0:
            self.ban_count = 190
            self.kill_zombie()

        if keys[pygame.K_d] and not keys[pygame.K_a]:
            self.world_shift = self.speed

        elif keys[pygame.K_a] and not keys[pygame.K_d]:
            self.world_shift = -self.speed

        else:
            self.world_shift = 0

        self.world_tiles_offset += self.world_shift

    def kill_zombie(self):
        for sprite in self.zombie1_sprites.sprites() + self.zombie2_sprites.sprites() + self.zombie3_sprites.sprites() + self.zombie4_sprites.sprites():
            if abs(sprite.rect.centerx - self.player_sprite.sprite.rect.centerx) < 85:
                sprite.kill()

    def check_walls_collisions(self):
        for sprite in self.zombie1_sprites.sprites() + self.zombie2_sprites.sprites() + self.zombie3_sprites.sprites() + self.zombie4_sprites.sprites():
            if pygame.sprite.spritecollide(sprite, self.wall_sprites, False):
                sprite.reverse_speed()

    def check_character_collisions(self):
        if pygame.sprite.spritecollide(self.player_sprite.sprite, self.zombie1_sprites, False):
            self.player_health -= 1
        if pygame.sprite.spritecollide(self.player_sprite.sprite, self.zombie2_sprites, False):
            self.player_health -= 2
        if pygame.sprite.spritecollide(self.player_sprite.sprite, self.zombie3_sprites, False):
            self.player_health -= 5
        if pygame.sprite.spritecollide(self.player_sprite.sprite, self.zombie4_sprites, False):
            self.player_health -= 30

    def check_situation(self):
        self.ban_count -= 1

        if self.ban_count < 0:
            self.ban_count = 0

        if self.player_health <= 0:
            pygame.quit()
            sys.exit()

    def get_zombies_count(self):
        return (len(self.zombie1_sprites.sprites()), len(self.zombie2_sprites.sprites()),
                len(self.zombie3_sprites.sprites()), len(self.zombie4_sprites.sprites()))

    def run(self):
        self.health.show_health(self.player_health)
        self.task.show_task(*self.get_zombies_count())

        if self.ban_count:
            self.ban.show_ban(self.ban_count)

        self.check_situation()
        self.get_input()
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

        self.wall_sprites.update(self.world_shift)

        self.zombie1_sprites.update(self.world_shift)
        self.zombie2_sprites.update(self.world_shift)
        self.zombie3_sprites.update(self.world_shift)
        self.zombie4_sprites.update(self.world_shift)
        self.check_walls_collisions()
        self.check_character_collisions()
        self.zombie1_sprites.draw(self.display_surface)
        self.zombie2_sprites.draw(self.display_surface)
        self.zombie3_sprites.draw(self.display_surface)
        self.zombie4_sprites.draw(self.display_surface)
