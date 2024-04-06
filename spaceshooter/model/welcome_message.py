import pygame


class WelcomeMessage:
    def __init__(self):
        self.font = font = pygame.font.Font(None, 36)
        self.surf = font.render("Welcome to SpaceShooter", True, "white")
        self.rect = self.surf.get_rect(center=(200,
                                               250))

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
