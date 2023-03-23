import sys
import pygame

class BlockWars:
    """Overall class to manage assets and behavior"""

    def __init__(self):
        """Initialize game, and create game resources"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((600,400))
        pygame.display.set_caption("Block Wars")
        
        # Set the background color
        self.bg_color = (230,230,230)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redarw the sreen during each pass through the loop
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game
    bw = BlockWars()
    bw.run_game()
