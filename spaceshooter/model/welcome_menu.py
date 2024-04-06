import pygame

from model.button import Button
from model.welcome_message import WelcomeMessage


class WelcomeMenu:
    def __init__(self):
        self.welcome_message = WelcomeMessage()
        self.start_img = (pygame.image.load(
            '/home/bloodwolf/project/python/pyExperaments/spaceshooter/image/start-1.png')).convert_alpha()
        self.exit_img = (pygame.image.load(
            '/home/bloodwolf/project/python/pyExperaments/spaceshooter/image/exit-1.png')).convert_alpha()

        self.start_button = Button(150,
                                   300, self.start_img, 0.5)

