class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialise statistics"""
        self.settings = ai_game.settings
        self._reset_stats()
        #start the game in inactive state
        self.game_active = False
        # High score should never be reset
        self.high_score = 0

    def _reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
