import pygame
import random
import time
from pygame.sprite import Sprite

class RedBlock(Sprite):
    """ Class to manage the red block """

    def __init__(self, bw_game):
        # Initialize
        super().__init__()
        self.screen = bw_game.screen
        self.settings = bw_game.settings
        self.level = bw_game.game_stats.level

        # Load the image
        self.image = pygame.image.load('images/red_block.bmp')
        self.image = pygame.transform.scale(self.image, (self.settings.red_block_width, self.settings.red_block_height))
        self.rect = self.image.get_rect()

        # Starting position at left top
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height*4

        # Initial velocity
        v0       = self.settings.red_block_speed
        self.vx0 = v0
        self.vy0 = v0*0.25
        self.vx  = 0
        self.vy  = 0

        # Coordinate in float
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # Move direction
        self.vx_dir = 1

        # Current time
        self.t0 = time.time()
        self.t_rand = self.t0
        self.t_next_fire = self.t0 
        self.update_t_next_fire()

    def update(self):
        # Random velocity
        if time.time()>self.t_rand+random.random()*30:
            self.t_rand = time.time()
            r1 = (random.random()-0.5)*2
            r2 = random.random()
            self.vx = self.vx0*(1+self.level)*r1*0.2
            self.vy = self.vy0*(1+self.level)*r2*0.2

        # Move
        self.x += self.vx
        self.y += self.vy

        # Bounce from wall
        if self.x>= self.settings.screen_width:
            if self.vx>0:
                self.y += self.rect.height*0.25
                self.vx *= -1
        elif self.x<= 0:
            if self.vx<0:
                self.y += self.rect.height*0.25
                self.vx *= -1

        # Coordinate on screen
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
    
    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update_t_next_fire(self):
        self.t_next_fire += self.settings.bullet_dt*1000 \
                *random.random()/self.level

