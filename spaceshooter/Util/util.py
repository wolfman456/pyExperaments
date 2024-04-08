import pygame

from Util.screen_util import game_over

running = True


def self_check_bounds(self, game_object):
    if self.rect.left < 0:
        self.rect.left = 0

    if self.rect.right > game_object.screen.get_width():
        self.rect.right = game_object.screen.get_width()


def check_collision(game_object):
    global running
    if pygame.sprite.spritecollideany(game_object.player, game_object.enemies):
        game_object.player.kill()
        game_over(game_object)
        running = False
    pygame.sprite.groupcollide(game_object.bullets, game_object.enemies, True, True)


def get_is_running():
    return running


