import pygame

from model import player
from model.enemy import Enemy


class ShooterObject:
    def __init__(self):
        self._init_game()
        self.screen = pygame.display.set_mode((800, 600))
        self.player = player.Player()
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.all_sprites.add(self.player, self.enemies,self.bullets)
        self.timer = pygame.time.Clock()
        self.score = 0
        self.ADD = pygame.USEREVENT + 1


    def _load_screen(self):
        print("here")
        font = pygame.font.Font(None, 36)
        welcome = font.render("Welcome", True, "white")
        self.screen.blit(welcome, (self.screen.get_width() / 2, self.screen.get_height() / 2))
        pygame.display.flip()

    def main_loop(self):
        pygame.time.set_timer(self.ADD, 500)
        while True:
            self._handle_input()

            self._process_game_logic()

            self._draw()

    def _draw(self):
        self.player.update(self)
        self.bullets.update()
        self.enemies.update()
        self.screen.fill((0, 0, 0))
        for entity in self.all_sprites:
            self.screen.blit(entity.surf, entity.rect)
        pygame.display.flip()
        self.timer.tick(60)

    def _init_game(self):
        pygame.init()
        pygame.display.set_caption('Space shooter')

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
            if event.type == self.ADD:
                enemy = Enemy(self)
                self.enemies.add(enemy)
                self.all_sprites.add(self.enemies)
            self.keys = pygame.key.get_pressed()

    def _process_game_logic(self):
        pass


if __name__ == '__main__':
    shooter = ShooterObject()
    shooter.main_loop()
