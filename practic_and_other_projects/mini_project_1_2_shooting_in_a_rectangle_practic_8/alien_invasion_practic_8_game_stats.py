class GameStats():
    """Отслеживает статистики для игры Alien Invasion"""
    def __init__(self, ai_practic):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.settings = ai_practic.settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.bullets_left = self.settings.bullets_limit