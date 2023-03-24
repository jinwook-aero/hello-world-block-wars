import pygame

class GreenBlock:
    """ Class to manage the green block """

    def __init__(self, bw_game):
        # Initialize
        self.screen = bw_game.screen
        self.screen_rect = bw_game.screen.get_rect()
        self.settings = bw_game.settings

        # Load the image
        self.image = pygame.image.load('images/green_block.bmp')
        self.image = pygame.transform.scale(self.image, (self.settings.green_block_width, self.settings.green_block_height))
        self.rect = self.image.get_rect()

        # Start at the bottom center
        self.rect.midbottom = self.screen_rect.midbottom

        # Coordinate in float
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Motion flag
        self.moving_right = False
        self.moving_left  = False
        self.moving_up    = False
        self.moving_down  = False

    def update(self):
        if self.moving_right and self.x < self.screen_rect.right - self.settings.green_block_width:
            self.x += self.settings.green_block_speed
        elif self.moving_left and self.x > self.screen_rect.left:
            self.x -= self.settings.green_block_speed
        elif self.moving_up and self.y > self.screen_rect.top:
            self.y -= self.settings.green_block_speed
        elif self.moving_down and self.y < self.screen_rect.bottom - self.settings.green_block_height:
            self.y += self.settings.green_block_speed
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        
    def draw(self):
        # Draw the block
        self.screen.blit(self.image, self.rect)
