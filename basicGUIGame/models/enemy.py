import random
import pygame
from pygame import sprite, Surface

SCORE = 0


def score():
    global SCORE
    SCORE += 1


def get_score():
    return SCORE


def display_score(screen):
    font = pygame.font.Font(None, 36)
    dis_score = get_score()
    score_text = font.render(f"Score: {dis_score}", True, "white")
    screen.blit(score_text, (10, 10))


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
