from pygame import sprite, Surface
from pygame.locals import *


class Player(sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = Surface((75, 25))
        self.surf.fill("red")
        self.rect = self.surf.get_rect(center=(400, 400))

    def update(self, pressed_keys, SCREEN_WIDTH, SCREEN_HEIGHT):
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN] or pressed_keys[K_s]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            self.rect.move_ip(5, 0)

        # Check to see if player hit edge.
        self.self_checkBounds(SCREEN_WIDTH, SCREEN_HEIGHT)

    def self_checkBounds(self, width, height):
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > width:
            self.rect.right = width

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= height:
            self.rect.bottom = height
