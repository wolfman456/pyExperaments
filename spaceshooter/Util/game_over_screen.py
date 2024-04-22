import pygame
import pygame_gui
import sys

from Util.high_score_util import HighScore


class GameOver:
    def __init__(self, x, y, width, height, game_object):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.game_object = game_object
        self.ui_refresh = self.game_object.timer.tick(60) / 1000
        self.manager = pygame_gui.UIManager(self.game_object.screen_size)
        self.high_score = HighScore()
        pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((self.x, self.y), (self.width, self.height)),
            manager=self.manager,
            object_id='#main_text_entry')

    def main(self):
        while True:
            self._handle_input()
            self._draw()

    def _draw(self):
        self.manager.update(self.ui_refresh)
        pygame.display.update()
        self.game_object.screen.fill((0, 0, 0))
        self.manager.draw_ui(self.game_object.screen)
        pygame.display.update()

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                    event.ui_object_id == '#main_text_entry'):
                self.high_score.player_name = event.text
                self.high_score.score = self.game_object.score.score
                print(self.game_object.score.score)
                self.high_score.save()

            self.manager.process_events(event)