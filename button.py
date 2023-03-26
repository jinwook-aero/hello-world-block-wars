import pygame.font

class Button():

    def __init__(self, bw_game, msg, width_ratio, height_ratio):
        """ Initialize button attributes """
        self.screen = bw_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = bw_game.settings

        # Dimensions
        self.width = int(self.settings.screen_width*width_ratio)
        self.height = int(self.settings.screen_height*height_ratio)
        self.button_color = (25, 175, 175)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        # Message
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(
           msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

