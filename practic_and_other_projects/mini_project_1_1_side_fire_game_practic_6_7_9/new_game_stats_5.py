import json

class GameStats():
    """Отслеживает статистики для игры Alien Invasion"""
    def __init__(self, ai_practic):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.settings = ai_practic.settings
        self.reset_stats()

        self.game_active = False #игра запускается в активном состоянии

        self.filename = 'learning_python_erik_matiz\\part_2\\project1_game\\game_projects_and_practic\\practic_and_other_projects\\mini_project_1_1_side_fire_game_practic_6_7_9\\high_score_practic.json'
        
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
        self.level = 0