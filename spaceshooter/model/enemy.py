import random

import pygame
from pygame import sprite
from pygame.locals import RLEACCEL


class Enemy(sprite.Sprite):
    def __init__(self, game_object):
        sprite.Sprite.__init__(self)
        self.surf = pygame.image.load(
            "/home/bloodwolf/project/python/pyExperaments/spaceshooter/model/enemy.py").convert_alpha()
        self.rect = pygame.transform.scale(self.surf, (20, 30))

        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        self.rect = self.surf.get_rect(
            center=(
                random.randint(30, game_object.screen.get_width() - 30),
                30

            )
        )

        self.speed = 5

    def update(self):
        self.rect.move_ip(0, +self.speed)
        if self.rect.top < 0:
            self.kill()
            # score()
