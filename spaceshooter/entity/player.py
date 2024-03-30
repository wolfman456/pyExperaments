import pygame
from pygame.locals import RLEACCEL, K_LEFT, K_a, K_d, K_RIGHT

from Util.util import self_check_bounds


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("/home/bloodwolf/project/python/pyExperaments/spaceshooter/resources/SpaceShipSmall.png").convert()

        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        self.rect = self.surf.get_rect(center=(400, 550))

    def update(self, event, game_object):
        if event.keys[K_LEFT] or event.keys[K_a]:
            self.rect.move_ip(-5, 0)
        if event.keys[K_RIGHT] or event.keys[K_d]:
            self.rect.move_ip(5, 0)

        self_check_bounds(self, game_object)
