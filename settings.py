class Settings:
    """A class to store all settings"""

    def __init__(self):
        """Initialize setting"""
        # Screen
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230,230,230)
        self.is_full_screen = False
        
        # Green block
        self.green_block_speed = 0.2
        self.green_block_width = 20
        self.green_block_height = 20

        # Bullet
        self.bullet_speed = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_max = 3
