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

        self.direct = 0
        self.helpanim = 0
        self.animation = [pygame.image.load(path).convert_alpha() for path in
                          ['../map/character/run/right.png', '../map/character/run/right2.png',
                           '../map/character/run/left.png', '../map/character/run/left2.png',
                           '../map/character/run/jump_left.png', '../map/character/run/jump_right.png',
                           '../map/character/run/r1.png', '../map/character/run/l1.png']]

        self.on_ground = True
        self.direct = True

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
            if not keys[pygame.K_SPACE]:
                self.image = self.current_image
                self.current_image = self.animation[0]
                self.current_image = self.animation[0 + self.helpanim // 5]
                self.helpanim = (self.helpanim + 1) % 10
                self.direct = True

            else:
                self.image = self.current_image
                self.current_image = self.animation[5]
                self.lastkey = keys[pygame.K_d]
                self.direct = True


        elif keys[pygame.K_a] and not keys[pygame.K_d]:
            if not keys[pygame.K_SPACE]:
                self.image = self.current_image
                self.current_image = self.animation[2]
                self.current_image = self.animation[2 + self.helpanim // 5]
                self.helpanim = (self.helpanim + 1) % 10
                self.lastkey = keys[pygame.K_a]
                self.direct = False
            else:
                self.image = self.current_image
                self.current_image = self.animation[4]
                self.lastkey = keys[pygame.K_a]
                self.direct = False

        elif pygame.KEYUP:
            if self.direct:
                self.image = self.current_image
                self.current_image = self.animation[6]
            else:
                self.image = self.current_image
                self.current_image = self.animation[7]

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
