import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, path_to_image):
        super().__init__()
        self.current_image = pygame.image.load(path_to_image).convert_alpha()
        self.image = self.current_image
        self.rect = self.image.get_rect(topleft=pos)

        self.y_direction = 0
        self.gravity = 1.2
        self.jump_speed = -16

        self.on_ground = True

    def apply_gravity(self):
        self.y_direction += self.gravity
        self.rect.y += self.y_direction

    def jump(self):
        self.y_direction = self.jump_speed

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()

        if keys[pygame.K_d] and not keys[pygame.K_a]:
            self.image = self.current_image

        if keys[pygame.K_a] and not keys[pygame.K_d]:
            self.image = pygame.transform.flip(self.current_image, True, False)

    def vertical_collisions(self, new_y):
        if self.y_direction > 0:
            self.rect.bottom = new_y
            self.on_ground = True

        elif self.y_direction < 0:
            self.rect.top = new_y

        self.y_direction = 0

    def update(self):
       self.get_input()
       self.apply_gravity()
       self.on_ground = False
