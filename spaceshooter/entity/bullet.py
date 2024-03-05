from pygame import sprite, Surface


class Bullet(sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
        self.surf = Surface((10, 10))
        self.surf.fill("red")
        self.rect = self.surf.get_rect(center=(
            0,
            550
        ))

        self.speed = 15
