class GameStats:
    def __init__(self, bw_game):
        self.settings = bw_game.settings
        self.max_score = 0
        self.is_active = False
        self.life = self.settings.life_limit
        self.score = 0

    def reset_stats(self):
        self.score = 0
        self.life = self.settings.life_limit
