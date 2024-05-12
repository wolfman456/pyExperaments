import pygame
import pygame_gui
import sys

from Util.high_score_util import HighScore


GAME_OVER = True

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
        font = pygame.font.Font(None, 36)
        self.game_over_text = font.render("GAME OVER", True, "white")

        pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((self.x, self.y), (self.width, self.height)),
            manager=self.manager,
            object_id='#main_text_entry', initial_text="Name")

    def main(self):
        while True:
            self._handle_input()
            self._draw()

    def _draw(self):
        while GAME_OVER:
            self.manager.update(self.ui_refresh)
            self.game_object.screen.fill((0, 0, 0))
            self.manager.draw_ui(self.game_object.screen)
            self.game_object.screen.blit(
                self.game_over_text, (
                    self.game_object.screen.get_width() / 2 - 75, self.game_object.screen.get_height() / 2 - 40)
            )
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
