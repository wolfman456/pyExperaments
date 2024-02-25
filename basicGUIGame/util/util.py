import pygame

from models.enemy import get_score


def timer(screen):
    font = pygame.font.Font(None, 36)
    clock = pygame.time.get_ticks() // 1000
    clock_text = font.render(f'Elapsed time: {clock}', True, 'white')
    screen.blit(clock_text, (580, 10))


def display_score(screen):
    font = pygame.font.Font(None, 36)
    dis_score = get_score()
    score_text = font.render(f"Score: {dis_score}", True, "white")
    screen.blit(score_text, (10, 10))
