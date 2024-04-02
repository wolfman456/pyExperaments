import pygame

from Util.util import add_enemy, draw_to_screen, check_collision
from model import player
from model.enemy import Enemy


class ShooterObject:
    def __init__(self):
        self._init_game()
        self.game_loop = False
        self.welcome_loop = True
        self.screen = pygame.display.set_mode((800, 600))
        self.player = player.Player()
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.all_sprites.add(self.player, self.enemies, self.bullets)
        self.timer = pygame.time.Clock()
        self.score = 0
        self.ADD = pygame.USEREVENT + 1

    def _load_screen(self):
        font = pygame.font.Font(None, 36)
        welcome = font.render("Welcome", True, "white")
        self.screen.blit(welcome, (self.screen.get_width() / 2 - 20, self.screen.get_height() / 2))
        pygame.display.flip()

    def main_loop(self):

        while self.welcome_loop:
            self._handle_input()
            self._load_screen()

        pygame.time.set_timer(self.ADD, 500)
        while self.game_loop:
            self._handle_input()

            self._process_game_logic()

            self._draw()

    def _draw(self):
        draw_to_screen(self)

    def _init_game(self):
        pygame.init()
        pygame.display.set_caption('Space shooter')

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
            add_enemy(self, event)
            self.keys = pygame.key.get_pressed()

    def _process_game_logic(self):
        check_collision(self)
