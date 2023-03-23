import sys
import pygame
from settings import Settings
from green_block import GreenBlock

class BlockWars:
    """Overall class to manage assets and behavior"""

    def __init__(self):
        """Initialize game, and create game resources"""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
                (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Block Wars")

        self.green_block = GreenBlock(self)
        
        # Set the background color
        self.bg_color = (230,230,230)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.green_block.update()
            self._update_screen()


    def _check_events(self):
        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Quit
                if event.key == pygame.K_q:
                    sys.exit()
                   
                # Full screen
                if event.key == pygame.K_l:
                    if self.settings.is_full_screen == False:
                        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                        self.settings.screen_width = self.screen.get_rect().width
                        self.settings.screen_height = self.screen.get_rect().height
                        self.settings.is_full_screen = True
                    else: # if self.settings.is_full_screen = True: 
                        self.settings = Settings()
                        self.screen = pygame.display.set_mode(
                                        (self.settings.screen_width,self.settings.screen_height))

                # Move begin
                if event.key == pygame.K_RIGHT:
                    self.green_block.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.green_block.moving_left = True
                elif event.key == pygame.K_UP:
                    self.green_block.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.green_block.moving_down = True
            elif event.type == pygame.KEYUP:
                # Move end
                if event.key == pygame.K_RIGHT:
                    self.green_block.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.green_block.moving_left = False
                elif event.key == pygame.K_UP:
                    self.green_block.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.green_block.moving_down = False

    def _update_screen(self):
        # Redarw the sreen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.green_block.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game
    bw = BlockWars()
    bw.run_game()


