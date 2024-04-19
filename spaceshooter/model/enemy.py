import random

import pygame
from pygame import sprite
from pygame.locals import RLEACCEL


class Enemy(sprite.Sprite):
    def __init__(self, game_object):
        sprite.Sprite.__init__(self)
        self.game_object = game_object
        self.surf = pygame.image.load(
            "/home/bloodwolf/project/python/pyExperaments/spaceshooter/image/Spaceship004.png").convert_alpha()
        self.rect = pygame.transform.scale(self.surf, (20, 30))

        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        self.rect = self.surf.get_rect(
            center=(
                random.randint(30, self.game_object.screen.get_width() - 30),
                30

            )
        )

        self.speed = 5

    def update(self):
        self.rect.move_ip(0, +self.speed)
        if self.rect.top >= self.game_object.screen.get_height():
            self.kill()
            self.game_object.enemy_count -= 1