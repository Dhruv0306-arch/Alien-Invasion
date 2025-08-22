class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialise statistics"""
        self.settings = ai_game.settings
        self._reset_stats()
        #start the game in inactive state
        self.game_active = False

    def _reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.ship_left = self.settings.ship_limit
