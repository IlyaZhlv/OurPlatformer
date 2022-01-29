import pygame


class Zombie1(pygame.sprite.Sprite):
    def __init__(self, pos, path_to_image):
        super().__init__()
        self.current_image = pygame.image.load(path_to_image).set_colorkey('white')
        self.image = self.current_image
        self.rect = self.image.get_rect(topleft=pos)

        self.y_direction = 0
        self.gravity = 1.2
        self.jump_speed = -16

        self.on_ground = True
