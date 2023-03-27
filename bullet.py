import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Class to manage bullets from origin_block """

    def __init__(self, bw_game, origin_block, vy_factor):
        """ Create bullet object """
        super().__init__()
        self.screen = bw_game.screen
        self.settings = bw_game.settings

        # Create rectangle
        self.rect = pygame.Rect(0, 0, 
                self.settings.bullet_width,
                self.settings.bullet_height)
        self.rect.center = origin_block.rect.center

        # Speed
        self.vy = self.settings.bullet_speed*vy_factor

        # Color and minimum spacing
        if vy_factor < 0: # From green block
            self.bullet_color = self.settings.bullet_color_from_green
            self.rect.y -= self.settings.bullet_height
        else: # From red block
            self.bullet_color = self.settings.bullet_color_from_red
            self.rect.y += self.settings.bullet_height

        # Coordinate
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        self.y += self.vy
        self.rect.y = int(self.y)

    def draw(self):
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)
