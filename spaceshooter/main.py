import pygame
from pygame.locals import K_SPACE

from entity.bullet import Bullet
from entity.enemy import Enemy
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
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(enemies)
all_sprites.add(bullet_group)


def main():
    running = True
    pygame.init()
    ADD = pygame.USEREVENT + 1
    pygame.time.set_timer(ADD, 500)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == ADD:
                enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
                enemies.add(enemy)
                all_sprites.add(enemy)
        keys = pygame.key.get_pressed()

        if keys[K_SPACE]:
            print("key")
            bullet = Bullet(player.rect.left)
            bullet_group.add(bullet)
            all_sprites.add(bullet_group)

        player.update(keys, SCREEN_WIDTH)
        bullet_group.update()
        enemies.update()
        screen.fill((0, 0, 0))
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == '__main__':
    main()
