import json

class GameStats():
    """Отслеживает статистики для игры Alien Invasion"""
    def __init__(self, ai_game):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False #игра запускается в активном состоянии

        self.filename = 'learning_python_erik_matiz\\part_2\\project1_game\\game_projects_and_practic\\project_1_3_alien_invasion_full_game\\high_score.json'

        #рекорд не должен сбрасываться

        self.check_old_record()

    def check_old_record(self):
        try:
            with open(self.filename) as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
            self.high_score = 0

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1