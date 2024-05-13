import pygame

TITLE = "Break It"
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000


class GameObject:

    def __init__(self):
        self._init_game()
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT

    def _init_game(self):
        pygame.init()
        pygame.display.set_caption(TITLE)

    def mainloop(self):
        while True:
            pass
