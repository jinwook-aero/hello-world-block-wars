import pygame
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
        self._prep_score()

    def _prep_score(self):
        # Strings
        score_str = str(self.stats.score)
        max_str   = str(self.stats.max_score)
        level_str = str(self.stats.level)

        # Images
        self.score_image = self.font.render(
                score_str, True, self.text_color, self.settings.bg_color)
        self.max_image = self.font.render(
                max_str, True, self.text_color, self.settings.bg_color)
        self.level_image = self.font.render(
                level_str, True, self.text_color, self.settings.bg_color)

        # Display
        self.score_rect = self.score_image.get_rect()
        self.score_rect.x = self.screen_rect.right - self.score_rect.width - 15
        self.score_rect.y = 15

        self.max_rect = self.max_image.get_rect()
        self.max_rect.x = int((self.screen_rect.left + self.screen_rect.right)/2)
        self.max_rect.y = 15

        self.level_rect = self.level_image.get_rect()
        self.level_rect.x = self.screen_rect.right - self.level_rect.width - 15
        self.level_rect.y = 45

        # Life count
        self.life_images = []
        self.life_rects  = []
        for n in range(self.stats.life):
            # Load the image
            image = pygame.image.load('images/green_block.bmp')
            image = pygame.transform.scale(image, 
                     (self.settings.green_block_width, self.settings.green_block_height))
            rect = image.get_rect()

            # Set position
            rect.x = rect.width*(2*n+1)
            rect.y = rect.height

            # Append to list
            self.life_images.append(image)
            self.life_rects.append(rect)

    def draw(self):
        self._prep_score()
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.max_image, self.max_rect)
        self.screen.blit(self.level_image, self.level_rect)
        for n in range(self.stats.life):
            self.screen.blit(self.life_images[n], self.life_rects[n])
