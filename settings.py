class Settings:
    """A class to store all settings"""

    def __init__(self):
        """Initialize setting"""
        # Screen
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230,230,230)
        self.is_full_screen = False

        # Frame per second
        self.frame_per_second = 120
        
        # Life
        self.life_limit = 1

        # Green block
        self.green_block_speed = 600/self.frame_per_second
        self.green_block_width = 20
        self.green_block_height = 20

        # Red block
        self.red_block_speed = 300/self.frame_per_second
        self.red_block_width = 20
        self.red_block_height = 20
        self.red_block_point = 100

        # Bullet
        self.bullet_speed = 1200/self.frame_per_second
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_max = 1000
        self.bullet_dt = 0.05
