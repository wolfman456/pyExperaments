import pygame


class ShooterObject:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))

    def _load_screen(self):
        print("here")
        font = pygame.font.Font(None, 36)
        welcome = font.render("Welcome", True, "white")
        self.screen.blit(welcome, (self.screen.get_width() / 2, self.screen.get_height() / 2))
        pygame.display.flip()

    def main_loop(self):

        while True:
            self._load_screen()

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()

    def _process_game_logic(self):
        pass


if __name__ == '__main__':
    shooter = ShooterObject()
    shooter.main_loop()
