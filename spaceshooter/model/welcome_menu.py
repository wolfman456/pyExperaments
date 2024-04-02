import pygame


class WelcomeMenu:
    def __init__(self):
        self.font = font = pygame.font.Font(None, 36)
        self.text = font.render("Welcome to SpaceShooter", 36)
