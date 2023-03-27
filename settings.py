class Settings:
    """A class to store all settings"""

    def __init__(self):
        """Initialize setting"""
        # Screen
        self.screen_width = 600
        self.screen_height = 450
        self.bg_color = (230,230,230)
        self.is_full_screen = False

        # Frame per second
        self.frame_per_second = 360
        
        # Life
        self.life     = 2
        self.life_max = 5

        # Level
        self.level = 1
        
        # Green block
        self.green_block_speed = 20/self.frame_per_second
        self.green_block_width = 20
        self.green_block_height = 20

        # Red block
        self.red_block_speed = 300/self.frame_per_second
        self.red_block_width = 20
        self.red_block_height = 20
        self.red_block_point = 100

        # Bullet
        self.bullet_speed = 1600/self.frame_per_second
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_max = 1000
        self.bullet_dt = 0.05

        self.bullet_color_from_green = (100,200,100)
        self.bullet_color_from_red   = (200,100,100)
