import pygame


class Health:
    def __init__(self, surface):
        self.display_surface = surface

        self.font = pygame.font.Font('../map/ARCADEPI.TTF', 40)

    def show_health(self, amount):
        amount_surface = self.font.render(str(amount), False, 'red')
        amount_rect = amount_surface.get_rect(topleft=(30, 30))
        self.display_surface.blit(amount_surface, amount_rect)
