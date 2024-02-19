import pygame
from pygame.locals import *

from models.entity import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Basic Pygame')

    running = True

    pygame.display.flip()
    player = Player()
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
        pressed_key = pygame.key.get_pressed()
        # probably need to reverse at some point
        player.update(pressed_key, SCREEN_WIDTH, SCREEN_HEIGHT)

        screen.blit(player.surf, player.rect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
