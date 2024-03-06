def self_check_bounds(self, width):
    if self.rect.left < 0:
        self.rect.left = 0

    if self.rect.right > width:
        self.rect.right = width

# def fire_bullet():
#
