import random

from pygame import sprite, Surface, locals


class Enemy(sprite.Sprite):
    def __init__(self, width, height):
        super(Enemy, self).__init__()
        self.surf = Surface((20, 20))
        self.surf.fill("blue")