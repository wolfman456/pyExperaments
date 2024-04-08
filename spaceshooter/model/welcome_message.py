import pygame


class WelcomeMessage:
    def __init__(self, game_object):
        self.font = font = pygame.font.Font(None, 36)
        self.surf = font.render("Welcome to SpaceShooter", True, "white")
        self.rect = self.surf.get_rect(center=(game_object.screen.get_width() / 2, game_object.screen.get_height() / 2))

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
