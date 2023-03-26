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
        # Strings
        score_str = str(self.stats.score)
        max_str = str(self.stats.max_score)
        life_str = "Life: " + str(self.stats.life)

        # Images
        self.score_image = self.font.render(
                score_str, True, self.text_color, self.settings.bg_color)
        self.max_image = self.font.render(
                max_str, True, self.text_color, self.settings.bg_color)
        self.life_image = self.font.render(
                life_str, True, self.text_color, self.settings.bg_color)

        # Display
        self.score_rect = self.score_image.get_rect()
        self.score_rect.x = self.screen_rect.right - self.score_rect.width - 15
        self.score_rect.y = 15

        self.max_rect = self.max_image.get_rect()
        self.max_rect.x = int((self.screen_rect.left + self.screen_rect.right)/2)
        self.max_rect.y = 15

        self.life_rect = self.life_image.get_rect()
        self.life_rect.x = self.screen_rect.left + 15
        self.life_rect.y = 15

    def draw(self):
        self.prep_score()
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.max_image, self.max_rect)
        self.screen.blit(self.life_image, self.life_rect)
