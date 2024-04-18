import pygame


class Score:
    def __init__(self, game_object):
        self.game_object = game_object
        self.score = 0
        self.font = pygame.font.Font(None, 30)
        self.score_txt = self.font.render("something", True, "white")

    def increment(self):
        self.score += 1

    def draw(self):
        self.game_object.screen.blit(self.score_txt, (30, 30))
