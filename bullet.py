import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ Class to manage bullets from the ship """

    def __init__(self, bw_game):
        """ Create bullet objecdt """
        super().__init__()
        self.screen = bw_game.screen
        self.settings = bw_game.settings

        # Create rectangle
        self.rect = pygame.Rect(0, 0, 
                self.settings.bullet_width,
                self.settings.bullet_height)
        self.rect.midtop = bw_game.green_block.rect.midtop
        
        # Coordinate
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = int(self.y)

    def draw(self):
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)
