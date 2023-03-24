import pygame
from pygame.sprite import Sprite

class RedBlock(Sprite):
    """ Class to manage the red block """

    def __init__(self, bw_game):
        # Initialize
        super().__init__()
        self.screen = bw_game.screen
        self.settings = bw_game.settings

        # Load the image
        self.image = pygame.image.load('images/red_block.bmp')
        self.image = pygame.transform.scale(self.image, (self.settings.red_block_width, self.settings.red_block_height))
        self.rect = self.image.get_rect()

        # Start at the bottom center
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Coordinate in float
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def draw(self):
        self.screen.blit(self.image, self.rect)
