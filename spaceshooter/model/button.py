import pygame
import pygame_gui

from model.welcome_message import WelcomeMessage


class Button(WelcomeMessage):
    def __init__(self, button_message):
        super().__init__()
        self.manger = pygame_gui.UIManager((self.screen.width(), self.screen.height()))
        self.button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
            (self.screen.width() / 2, self.screen.height() / 2), (100, 20)),
            text=button_message, manager=self.manger)
