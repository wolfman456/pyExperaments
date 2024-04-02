import time

import pygame

running = True


def self_check_bounds(self, game_object):
    if self.rect.left < 0:
        self.rect.left = 0

    if self.rect.right > game_object.screen.get_width():
        self.rect.right = game_object.screen.get_width()


def check_collision(player, enemies, bullet_group, screen, width, height):
    global running
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        game_over(screen, width, height)
        running = False
    pygame.sprite.groupcollide(bullet_group, enemies, True, True)


def get_is_running():
    return running


def game_over(screen, width, height):
    font = pygame.font.Font(None, 36)
    game_over_text = font.render("GAME OVER", True, "white")
    screen.blit(game_over_text, (width / 2 - 75, height / 2))
    pygame.display.flip()
    time.sleep(5)
