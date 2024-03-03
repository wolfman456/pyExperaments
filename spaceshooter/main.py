import pygame

from entity.player import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("space shooter")
clock = pygame.time.Clock()
dt = 0
player = Player()


def main():
    running = True
    pygame.init()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        player.update(keys, SCREEN_WIDTH, SCREEN_HEIGHT)

        screen.fill((0, 0, 0))
        screen.blit(player.surf, player.rect)
        pygame.display.flip()


if __name__ == '__main__':
    main()