import pygame


def self_check_bounds(self, game_object):
    if self.rect.left < 0:
        self.rect.left = 0
    if self.rect.right > game_object.screen.get_width():
        self.rect.right = game_object.screen.get_width()


def check_collision(game_object):
    if pygame.sprite.spritecollideany(game_object.player, game_object.enemies):
        game_object.player.kill()
        game_object.game_loop = False
        game_object.game_over.main()

    if pygame.sprite.groupcollide(game_object.bullets, game_object.enemies, True, True):
        game_object.score.increment()
        game_object.enemy_count -= 1

