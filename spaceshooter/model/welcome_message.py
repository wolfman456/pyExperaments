import pygame

from model.gameobject import ShooterObject


class WelcomeMessage(ShooterObject):
    def __init__(self):
        super().__init__()
        self.font = font = pygame.font.Font(None, 36)
        self.surf = font.render("Welcome to SpaceShooter", True, "white")
        self.rect = self.surf.get_rect(center=(self.screen.get_width() / 2 - 30,
                                               self.screen.get_height() / 2))
