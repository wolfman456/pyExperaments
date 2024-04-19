import pygame
import time

from model.enemy import Enemy


def game_over(game_object):
    font = pygame.font.Font(None, 36)
    game_over_text = font.render("GAME OVER", True, "white")
    game_object.screen.blit(game_over_text, (game_object.screen.width / 2 - 75, game_object.screen.height / 2))
    pygame.display.flip()
    time.sleep(5)


def add_enemy(game_object, event):
    if event.type == game_object.ADD and len(game_object.enemies) <= 3:
        enemy = Enemy(game_object)
        game_object.enemies.add(enemy)
        game_object.all_sprites.add(game_object.enemies)
        game_object.enemy_count += 1


def draw_to_screen(game_object):
    game_object.player.update(game_object)
    game_object.bullets.update()
    game_object.enemies.update()
    game_object.screen.fill((0, 0, 0))
    for entity in game_object.all_sprites:
        game_object.screen.blit(entity.surf, entity.rect)


def draw_welcome(game_object):
    game_object.welcome_message.draw(game_object.screen)
    if game_object.exit_button.draw(game_object.screen):
        game_object.welcome_loop = False
    if game_object.high_score.draw(game_object.screen):
        print("high score")
    if game_object.start_button.draw(game_object.screen):
        game_object.welcome_loop = False
        game_object.game_loop = True
        game_object.screen.fill((0, 0, 0))
