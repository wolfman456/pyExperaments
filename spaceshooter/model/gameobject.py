import pygame

from Util.util import add_enemy, draw_to_screen, check_collision
from model import player
from model.button import Button
from model.welcome_message import WelcomeMessage


class ShooterObject:
    def __init__(self):
        self._init_game()
        self.time_delta = None
        self.game_loop = False
        self.welcome_loop = True
        self.screen = pygame.display.set_mode((800, 600))
        self.player = player.Player()
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.score = 0
        self.timer = pygame.time.Clock()
        self.ADD = pygame.USEREVENT + 1
        self.all_sprites.add(self.player, self.enemies, self.bullets)
        self.start_img = (pygame.image.load(
            '/home/bloodwolf/project/python/pyExperaments/spaceshooter/image/start-1.png')).convert_alpha()
        self.start_button = Button(100, 200, self.start_img, 0.8)
        self.welcome_message = WelcomeMessage()

    def main_loop(self):
        while self.welcome_loop:
            self._handle_input()
            self._draw()

        pygame.time.set_timer(self.ADD, 500)
        self.time_delta = self.timer.tick(60) / 1000.0
        while self.game_loop:
            self._handle_input()

            self._process_game_logic()

            self._draw()

    def _draw(self):
        if self.game_loop:
            draw_to_screen(self)
        if self.welcome_loop:
            self.welcome_message.draw(self.screen)
            if self.start_button.draw(self.screen):
                self.welcome_loop = False
                self.game_loop = True
                self.screen.fill((0, 0, 0))

        pygame.display.update()
        self.timer.tick(60)

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
