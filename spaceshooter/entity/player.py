import pygame
from pygame.locals import RLEACCEL, K_LEFT, K_a, K_d, K_RIGHT

from Util.util import self_check_bounds


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("resources/SpaceShipSmall.png").convert()

        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        self.rect = self.surf.get_rect(center=(400, 550))

    def update(self, keys, width):
        if keys[K_LEFT] or keys[K_a]:
            self.rect.move_ip(-5, 0)
        if keys[K_RIGHT] or keys[K_d]:
            self.rect.move_ip(5, 0)

        self_check_bounds(self, width)