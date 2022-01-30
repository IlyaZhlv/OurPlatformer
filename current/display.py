import pygame

from settings import screen_width


class Interface:
    def __init__(self, surface):
        self.display_surface = surface

        self.font = pygame.font.Font('../map/ARCADEPI.TTF', 40)

class Health(Interface):
    def __init__(self, surface):
        super().__init__(surface)

    def show_health(self, amount):
        amount_surface = self.font.render(str(amount), False, 'red')
        amount_rect = amount_surface.get_rect(topleft=(30, 30))
        self.display_surface.blit(amount_surface, amount_rect)


class Task(Interface):
    def __init__(self, surface):
        super().__init__(surface)

    def show_task(self, zombie1_count, zombie2_count, zombie3_count, zombie4_count):
        color = (34, 177, 76)

        zombie1_count_surface = self.font.render(str(zombie1_count), False, color)
        zombie2_count_surface = self.font.render(str(zombie2_count), False, color)
        zombie3_count_surface = self.font.render(str(zombie3_count), False, color)
        zombie4_count_surface = self.font.render(str(zombie4_count), False, color)

        zombie1_count_rect = zombie1_count_surface.get_rect(topleft=(screen_width - 100, 30))
        zombie2_count_rect = zombie2_count_surface.get_rect(topleft=(screen_width - 100, 90))
        zombie3_count_rect = zombie3_count_surface.get_rect(topleft=(screen_width - 100, 150))
        zombie4_count_rect = zombie4_count_surface.get_rect(topleft=(screen_width - 100, 210))

        for surface, rect in zip([zombie1_count_surface, zombie2_count_surface,
                                  zombie3_count_surface, zombie4_count_surface],
                                 [zombie1_count_rect, zombie2_count_rect,
                                  zombie3_count_rect, zombie4_count_rect]):
            self.display_surface.blit(surface, rect)

        zombie1_surface = pygame.transform.scale(pygame.image.load('../map/zombies/zombie1/1.png').convert_alpha(), (20, 45))
        zombie2_surface = pygame.transform.scale(pygame.image.load('../map/zombies/zombie2/1.png').convert_alpha(), (20, 45))
        zombie3_surface = pygame.transform.scale(pygame.image.load('../map/zombies/zombie3/1.png').convert_alpha(), (20, 45))
        zombie4_surface = pygame.transform.scale(pygame.image.load('../map/zombies/zombie4/1.png').convert_alpha(), (20, 45))

        self.display_surface.blit(zombie1_surface, zombie1_surface.get_rect(topleft=(screen_width - 140, 25)))
        self.display_surface.blit(zombie2_surface, zombie2_surface.get_rect(topleft=(screen_width - 140, 85)))
        self.display_surface.blit(zombie3_surface, zombie3_surface.get_rect(topleft=(screen_width - 140, 145)))
        self.display_surface.blit(zombie4_surface, zombie4_surface.get_rect(topleft=(screen_width - 140, 205)))


class Ban(Interface):
    def __init__(self, surface):
        super().__init__(surface)

    def show_ban(self, ban_count):
        ban_count_surface = self.font.render(str(ban_count), False, 'black')
        ban_count_rect = ban_count_surface.get_rect(topleft=(screen_width // 2 - 50, 30))
        self.display_surface.blit(ban_count_surface, ban_count_rect)
