class GameStats:
    def __init__(self, bw_game):
        self.settings = bw_game.settings
        self.max_score = 0
        self.is_active = False
        self.level    = self.settings.level
        self.life     = self.settings.life
        self.life_max = self.settings.life_max
        self.score = 0

    def reset_stats(self):
        self.score = 0
        self.level = self.settings.level
        self.life = self.settings.life
