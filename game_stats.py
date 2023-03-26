class GameStats:
    def __init__(self, bw_game):
        self.settings = bw_game.settings
        self.is_active = False
        self.life = self.settings.life_limit
        self.score = 0

    def reset_stats(self):
        self.is_active = True
        self.score = 0
        self.life = self.settings.life_limit
