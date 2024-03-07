import random

import pygame
from pygame import sprite
from pygame.locals import RLEACCEL


class Enemy(sprite.Sprite):
    def __init__(self, width, height):
        sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("resources/Spaceship004.png")
        self.rect = pygame.transform.scale(self.surf, (20, 30))

        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        self.rect = self.surf.get_rect(
            center=(
                random.randint(30, width - 30),
                30

            )
        )

        self.speed = 10

    def update(self):
        self.rect.move_ip(0, +self.speed)
        if self.rect.top < 0:
            self.kill()
            # score()
