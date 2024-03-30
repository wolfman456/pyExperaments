import pygame

from entity import player


class ShooterObject:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.player = player.Player()

    def _load_screen(self):
        print("here")
        font = pygame.font.Font(None, 36)
        welcome = font.render("Welcome", True, "white")
        self.screen.blit(welcome, (self.screen.get_width() / 2, self.screen.get_height() / 2))
        pygame.display.flip()

    def main_loop(self):

        while True:
            self._handle_input()

            self._process_game_logic()

            self._draw()

    def _draw(self):
        all_sprites = pygame.sprite.Group()
        all_sprites.add(self.player)
        self.screen.fill((0, 0, 0))
        for entity in all_sprites:
            self.screen.blit(entity.surf, entity.rect)
        pygame.display.flip()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption('Space shooter')

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
            event.keys = pygame.key.get_pressed()
            self.player.update(event, self.screen.get_width())

    def _process_game_logic(self):
        pass


if __name__ == '__main__':
    shooter = ShooterObject()
    shooter.main_loop()
