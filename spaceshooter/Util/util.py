import time

import pygame

from model.enemy import Enemy

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


def game_over(screen, width, height):
    font = pygame.font.Font(None, 36)
    game_over_text = font.render("GAME OVER", True, "white")
    screen.blit(game_over_text, (width / 2 - 75, height / 2))
    pygame.display.flip()
    time.sleep(5)


def add_enemy(game_object, event):
    if event.type == game_object.ADD:
        enemy = Enemy(game_object)
        game_object.enemies.add(enemy)
        game_object.all_sprites.add(game_object.enemies)


def draw_to_screen(game_object):
    game_object.player.update(game_object)
    game_object.bullets.update()
    game_object.enemies.update()
    game_object.screen.fill((0, 0, 0))
    for entity in game_object.all_sprites:
        game_object.screen.blit(entity.surf, entity.rect)
