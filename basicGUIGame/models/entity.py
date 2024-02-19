from pygame import sprite, Surface
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT


class Player(sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()


def update(self, pressed_keys, SCREEN_WIDTH, SCREEN_HEIGHT):
    if pressed_keys[K_UP]:
        self.rect.move_ip(0, -5)
    if pressed_keys[K_DOWN]:
        self.rect.move_ip(0, 5)
    if pressed_keys[K_LEFT]:
        self.rect.move_ip(-5, 0)
    if pressed_keys[K_RIGHT]:
        self.rect.move_ip(5, 0)

    # Keep player on the screen

    if self.rect.left < 0:
        self.rect.left = 0

    if self.rect.right > SCREEN_WIDTH:
        self.rect.right = SCREEN_WIDTH

    if self.rect.top <= 0:
        self.rect.top = 0

    if self.rect.bottom >= SCREEN_HEIGHT:
        self.rect.bottom = SCREEN_HEIGHT
