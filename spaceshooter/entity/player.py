import pygame
from pygame import Surface
from pygame.locals import RLEACCEL, K_LEFT, K_a, K_d, K_RIGHT


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        # self.surf = Surface((75, 25))
        # self.surf.fill("red")
        # self.rect = self.surf.get_rect(center=(400, 400))

        self.surf = pygame.image.load("resources/SpaceShipSmall.png").convert()

        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        self.rect = self.surf.get_rect(center=(400, 550))

    def update(self, keys, width, height):
        if keys[K_LEFT] or keys[K_a]:
            self.rect.move_ip(-5, 0)
        if keys[K_RIGHT] or keys[K_d]:
            self.rect.move_ip(5, 0)
