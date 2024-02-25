import random

from pygame import sprite, Surface

from util.util import score


class Enemy(sprite.Sprite):
    def __init__(self, width, height):
        super(Enemy, self).__init__()
        self.surf = Surface((30, 20))
        self.surf.fill("blue")
        self.rect = self.surf.get_rect(
            center=(
                random.randint(width + 20, width + 100),
                random.randint(0, height),
            )
        )
        self.speed = 15

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
            score()
