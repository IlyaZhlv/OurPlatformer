import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, path_to_image):
        super().__init__()
        self.image = pygame.image.load(path_to_image).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        self.y_direction = 0
        self.gravity = 0.8
        self.jump_speed = -16

    def apply_gravity(self):
        self.y_direction += self.gravity
        self.rect.y += self.y_direction

    def jump(self):
        self.y_direction = self.jump_speed

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.jump()

    def update(self):
       self.get_input()
       self.apply_gravity()
