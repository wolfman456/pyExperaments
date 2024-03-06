from pygame import sprite, Surface


class Bullet(sprite.Sprite):
    def __init__(self, player_x):
        super(Bullet, self).__init__()
        self.surf = Surface((10, 10))
        self.surf.fill("red")
        self.rect = self.surf.get_rect(center=(
            player_x + 48,
            525
        ))

        self.speed = 15

    def update(self):
        self.rect.move_ip(0, -self.speed)
        if self.rect.bottom < 0:
            self.kill()
