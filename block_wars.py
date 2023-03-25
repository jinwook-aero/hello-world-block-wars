import sys
import time
import pygame
from settings import Settings
from green_block import GreenBlock
from red_block import RedBlock
from bullet import Bullet

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
        self.red_blocks = pygame.sprite.Group()
        self.bullets =  pygame.sprite.Group()
        
        # Set the background color
        self.bg_color = (230,230,230)

        # Set the game
        self._create_red_blocks()

        # Set bullet firing frequency
        self.t_last_bullet = 0
        
        # t=0 and current time
        self.t0 = time.time()
        self.t  = self.t0
        self.frame_counter = 0

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Frame control
            tPass = self.t+1/self.settings.frame_per_second
            if time.time()>=tPass:
                # Time update
                self.t = time.time()
                self.frame_counter += 1

                # Update objects
                self._check_events()
                self.green_block.update()
                self.red_blocks.update()
                self._fire_bullet()
                self._update_bullets()
                
                # Ending check
                self._check_ending()

                # Update screen
                self._update_screen()
            else:
                continue

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

                # Fire begin
                if event.key == pygame.K_SPACE:
                    self.green_block.firing = True
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

                # Fire end
                if event.key == pygame.K_SPACE:
                    self.green_block.firing = False

    def _update_screen(self):
        # Redraw the sreen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.green_block.draw()
        for red_block in self.red_blocks.sprites():
            red_block.draw()
        for bullet in self.bullets.sprites():
            bullet.draw()

        # Make the most recently drawn screen visible
        pygame.display.flip()

    def _create_red_blocks(self):
        # Local self.settings = S
        S = self.settings

        # Row and columns of red blocks
        n_red_row = min(int(S.screen_height/S.red_block_height/2),2)
        n_red_col = int(S.screen_width/S.red_block_width/2)-1
        for n_row in range(n_red_row):
            for n_col in range(n_red_col):
                red_block = RedBlock(self)
                red_block.x += S.red_block_width*n_col*2
                red_block.y += S.red_block_height*n_row*2
                self.red_blocks.add(red_block)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

        # Collison check
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.red_blocks, True, True)
        
    def _fire_bullet(self):
        if self.green_block.firing \
                and len(self.bullets) <= self.settings.bullet_max \
                and time.time() >= self.t_last_bullet + self.settings.bullet_dt:
            self.t_last_bullet = time.time()
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_ending(self):
        # All kill
        isEnded = False
        if not self.red_blocks:
            isEnded = True
        elif pygame.sprite.spritecollideany(self.green_block, self.red_blocks):
            isEnded = True
        else:
            max_y = 0
            for red_block in self.red_blocks:
                max_y = max(max_y,red_block.y)
            if max_y>=self.settings.screen_height:
                isEnded = True

        if isEnded:
            # Purge
            self.red_blocks.empty()
            self.bullets.empty()
            
            # Recreate
            self._create_red_blocks()
            self.green_block = GreenBlock(self)

if __name__ == '__main__':
    # Make a game instance, and run the game
    bw = BlockWars()
    bw.run_game()
