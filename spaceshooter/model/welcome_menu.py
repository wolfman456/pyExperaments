import pygame


class WelcomeMenu(pygame.sprite.Sprite):
    def __init__(self, game_object):
        super(WelcomeMenu, self).__init__()
        self.font = font = pygame.font.Font(None, 36)
        self.surf = font.render("Welcome to SpaceShooter", True, "white")

        self.rect = self.surf.get_rect(center=(game_object.screen.get_width() / 2 - 30,
                                   game_object.screen.get_height() / 2))
