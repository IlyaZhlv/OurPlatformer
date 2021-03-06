import pygame

from random import randint, choice

from support import import_folder


class Zombie(pygame.sprite.Sprite):
    def __init__(self, pos, path_to_folder):
        super().__init__()
        self.frames = import_folder(path_to_folder)
        self.frame_index = 0

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        self.y_direction = 0
        self.gravity = 1.2
        self.jump_speed = -16

        self.on_ground = True

    def reverse_speed(self):
        self.speed *= -1

    def animation(self):
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        if self.speed > 0:
            self.image = self.frames[int(self.frame_index)]
        elif self.speed < 0:
            self.image = pygame.transform.flip(self.frames[int(self.frame_index)], True, False)

    def update(self, x_shift):
        self.rect.x -= x_shift
        self.rect.x += self.speed

        self.animation()


class Zombie1(Zombie):
    def __init__(self, pos, path_to_folder):
        super().__init__(pos, path_to_folder)

        self.speed = choice([-1, 1]) * randint(3, 5)


class Zombie2(Zombie):
    def __init__(self, pos, path_to_folder):
        super().__init__(pos, path_to_folder)

        self.speed = choice([-1, 1]) * randint(6, 8)


class Zombie3(Zombie):
    def __init__(self, pos, path_to_folder):
        super().__init__(pos, path_to_folder)

        self.speed = choice([-1, 1]) * randint(3, 7)


class Zombie4(Zombie):
    def __init__(self, pos, path_to_folder):
        super().__init__(pos, path_to_folder)

        self.speed = choice([-1, 1]) * randint(1, 2)
