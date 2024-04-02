import pygame
from pygame.locals import RLEACCEL, K_LEFT, K_a, K_d, K_RIGHT, K_SPACE
from model.bullet import Bullet

from Util.util import self_check_bounds


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("/home/bloodwolf/project/python/pyExperaments/spaceshooter/resources"
                                      "/SpaceShipSmall.png").convert()

        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        self.rect = self.surf.get_rect(center=(400, 550))

    def update(self, game_object):
        if game_object.keys[K_LEFT] or game_object.keys[K_a]:
            self.rect.move_ip(-10, 0)
        if game_object.keys[K_RIGHT] or game_object.keys[K_d]:
            self.rect.move_ip(10, 0)

        if game_object.keys[K_SPACE]:
            bullet = Bullet(self.rect.left)
            game_object.bullets.add(bullet)
            game_object.all_sprites.add(game_object.bullets)

        self_check_bounds(self, game_object)
