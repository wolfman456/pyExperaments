import pygame


class Score:
    def __init__(self, game_object):
        self.game_object = game_object
        self.score = 0
        self.font = pygame.font.Font(None, 30)

    def increment(self):
        self.score += 1

    def update(self):
        score_txt = self.font.render(f"Score : {self.score}", True, "white")
        self.game_object.screen.blit(score_txt, (30, 30))
