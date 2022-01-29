import pygame

from support import import_folder


class Zombie1(pygame.sprite.Sprite):
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

    def animation(self):
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, x_shift):
        self.rect.x -= x_shift

        self.animation()
