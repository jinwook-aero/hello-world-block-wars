import pygame.font
from pygame.sprite import Group
from green_block import GreenBlock

class Scoreboard:
    def __init__(self, bw_game):
        self.screen = bw_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = bw_game.settings
        self.stats = bw_game.game_stats

        # Font
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 24)

        # Score image
        self.prep_score()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
                score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.x = self.screen_rect.right - self.score_rect.width - 15
        self.score_rect.y = 15


    def draw(self):
        self.screen.blit(self.score_image, self.score_rect)
