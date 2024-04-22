import pygame

from Util.game_over_screen import GameOver
from Util.loadimage import load_image
from Util.screen_util import draw_welcome, draw_to_screen, add_enemy
from Util.util import check_collision
from model import player
from model.button import Button
from model.score import Score
from model.welcome_message import WelcomeMessage
import pygame_gui


class ShooterObject:
    def __init__(self):
        self._init_game()
        self.game_loop = False
        self.welcome_loop = True
        self.end_loop = False
        self.screen_size = (800, 600)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.player = player.Player()
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.score = Score(game_object=self)
        self.timer = pygame.time.Clock()
        self.ADD = pygame.USEREVENT + 1
        self.all_sprites.add(self.player, self.enemies, self.bullets)
        self.start_button = Button(self.screen.get_width() / 4, self.screen.get_height() / 2 + 40,
                                   load_image('start-1.png'), 0.8)
        self.exit_button = Button(self.screen.get_width() / 4 * 2 + 120, self.screen.get_height() / 2 + 40,
                                  load_image('exit-1.png'), 0.8)
        self.high_score = Button(self.screen.get_width() / 4 + 150, self.screen.get_height() / 2 + 40,
                                 load_image('high_score.png'), 0.8)
        self.welcome_message = WelcomeMessage(self)
        self.enemy_count = 0
        self.game_over = GameOver(x=self.screen.get_width() / 2-150, y=self.screen.get_height() / 2, game_object=self,
                                  width=300, height=40)

    def _init_game(self):
        pygame.init()
        pygame.display.set_caption('Space shooter')

    def main_loop(self):
        while self.welcome_loop:
            self._handle_input()
            self._draw()

        pygame.time.set_timer(self.ADD, 500)
        pygame.time.delay(1000)
        while self.game_loop:
            self._handle_input()

            self._process_game_logic()

            self._draw()
        while self.end_loop:
            pass

    def _draw(self):
        if self.game_loop:
            draw_to_screen(self)
            self.score.update()
        if self.welcome_loop:
            draw_welcome(self)

        pygame.display.update()
        self.timer.tick(60)

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.fire(self)
            add_enemy(self, event)
            self.keys = pygame.key.get_pressed()

    def _process_game_logic(self):
        check_collision(self)
