import pygame


class ShooterObject:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))

    def load_screen(self):
        pass

    def main_loop(self):
        while True:
            self._handle_input()

            self._process_game_logic()

            self._draw()

    def _draw(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption('Space shooter')

    def _handle_input(self):
        pass

    def _process_game_logic(self):
        pass


# if __name__ == '__main__':
#     shooter = ShooterObject()
#     shooter.main_loop()