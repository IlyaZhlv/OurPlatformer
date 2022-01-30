import pygame

from settings import screen_width

class Health:
    def __init__(self, surface):
        self.display_surface = surface

        self.font = pygame.font.Font('../map/ARCADEPI.TTF', 40)

    def show_health(self, amount):
        amount_surface = self.font.render(str(amount), False, 'red')
        amount_rect = amount_surface.get_rect(topleft=(30, 30))
        self.display_surface.blit(amount_surface, amount_rect)


class Task:
    def __init__(self, surface):
        self.display_surface = surface

        self.font = pygame.font.Font('../map/ARCADEPI.TTF', 40)

    def show_task(self, zombie1_count, zombie2_count, zombie3_count, zombie4_count):
        color = (34, 177, 76)

        zombie1_count_surface = self.font.render(str(zombie1_count), False, color)
        zombie2_count_surface = self.font.render(str(zombie2_count), False, color)
        zombie3_count_surface = self.font.render(str(zombie3_count), False, color)
        zombie4_count_surface = self.font.render(str(zombie4_count), False, color)

        zombie1_count_rect = zombie1_count_surface.get_rect(topleft=(screen_width - 100, 30))
        zombie2_count_rect = zombie1_count_surface.get_rect(topleft=(screen_width - 100, 90))
        zombie3_count_rect = zombie1_count_surface.get_rect(topleft=(screen_width - 100, 150))
        zombie4_count_rect = zombie1_count_surface.get_rect(topleft=(screen_width - 100, 210))

        for surface, rect in zip([zombie1_count_surface, zombie2_count_surface,
                                  zombie3_count_surface, zombie4_count_surface],
                                 [zombie1_count_rect, zombie2_count_rect,
                                  zombie3_count_rect, zombie4_count_rect]):
            self.display_surface.blit(surface, rect)