import pygame
import time

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
        self.rect.y -= self.rect.height

        # Coordinate in float
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Motion flag
        self.moving_right = False
        self.moving_left  = False
        self.moving_up    = False
        self.moving_down  = False

        # Default speed
        self.v0 = self.settings.green_block_speed

        # Current velocity
        self.vx = 0
        self.vy = 0

        # Accel t0
        self.ax_t0 = 0
        self.ay_t0 = 0

        # Firing flag
        self.firing = False

    def update(self):
        t_accel_max = 0.5
        # Horizontal accel
        if self.moving_right:
            if self.vx <= 0: # Accel started
                self.ax_t0 = time.time()
                dvx = self.v0-self.vx
            else:
                dt = time.time()-self.ax_t0
                dvx = +max(dt,t_accel_max)*self.v0
        elif self.moving_left:
            if self.vx >=0: # Accel started
                self.ax_t0 = time.time()
                dvx = -self.v0-self.vx
            else:
                dt = time.time()-self.ax_t0
                dvx = -max(dt,t_accel_max)*self.v0
        else: # Stop
            self.ax_t0 = time.time()
            dvx = -self.vx

        # Vertical accel
        if self.moving_up:
            if self.vy >= 0: # Accel started
                self.ay_t0 = time.time()
                dvy = -self.v0-self.vy
            else:
                dt = time.time()-self.ay_t0
                dvy = -max(dt,t_accel_max)*self.v0
        elif self.moving_down:
            if self.vy <=0: # Accel started
                self.ay_t0 = time.time()
                dvy = +self.v0-self.vy
            else:
                dt = time.time()-self.ay_t0
                dvy = +max(dt,t_accel_max)*self.v0
        else: # Stop
            self.ay_t0 = time.time()
            dvy = -self.vy
        
        # Speed update
        self.vx += dvx
        self.vy += dvy

        # Position update
        self.x += self.vx
        self.y += self.vy
        
        # Position limit
        xLeft   = self.screen_rect.left 
        xRight  = self.screen_rect.right - self.settings.green_block_width
        yTop    = self.screen_rect.top
        yBottom = self.screen_rect.bottom - self.settings.green_block_height

        self.x = min(max(self.x,xLeft),xRight)
        self.y = min(max(self.y,yTop),yBottom)

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        
    def draw(self):
        # Draw the block
        self.screen.blit(self.image, self.rect)
