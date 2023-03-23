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
