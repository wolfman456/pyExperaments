import time

import pygame

SCORE = 0


def score():
    global SCORE
    SCORE += 1


def get_score():
    return SCORE


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


def game_over(screen, width, height):
    font = pygame.font.Font(None, 36)
    game_over_text = font.render("GAME OVER", True, "white")
    screen.blit(game_over_text, (width / 2 - 75, height / 2))
    pygame.display.flip()
    time.sleep(10)

# possible furture use in another verison. will not be implemented in this version of this project
# def prepare_screen(screen, width, height):
#     screen.fill((0, 0, 0))
#     font = pygame.font.Font(None, 36)
#     prepare_text = font.render("Get Ready!", True, "white")
#     screen.blit(prepare_text, (width / 2 - 75, height / 2))
#     pygame.display.flip()
#     time.sleep(5)
