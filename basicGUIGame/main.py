import time

import pygame
from pygame.locals import *

from models.enemy import Enemy, display_score
from models.entity import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Basic Pygame')
    ADD = pygame.USEREVENT + 1

    pygame.time.set_timer(ADD, 500)
    running = True

    pygame.display.flip()
    player = Player()
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    text_surface = pygame.font.get_default_font()

    # Event loop
    while running:

        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == KEYDOWN:
                # If the Esc key is pressed, then exit the main loop
                if event.key == K_ESCAPE:
                    running = False
            # Check for QUIT event. If QUIT, then set running to false.
            elif event.type == QUIT:
                running = False

            elif event.type == ADD:
                # Create the new enemy and add it to sprite groups
                enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
                enemies.add(enemy)
                all_sprites.add(enemy)
        pressed_key = pygame.key.get_pressed()
        # probably need to reverse at some point
        player.update(pressed_key, SCREEN_WIDTH, SCREEN_HEIGHT)
        enemies.update()
        screen.fill((0, 0, 0))
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        print(pygame.time.get_ticks() // 1000, 'seconds elapsed')
        display_score(screen)
        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            running = False
        pygame.display.flip()
        pygame.time.Clock().tick(60)


if __name__ == "__main__":
    main()
