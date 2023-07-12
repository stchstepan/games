import pygame.font
from pygame.sprite import Sprite
import json

from ship import Ship

class Scoreboard:
    """Класс для вывода игровой информации"""
    def __init__(self, ai_game):
        """Иницифлизирует атрибуты подсчета очков"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.filename = 'learning_python_erik_matiz\\part_2\\project1_game\\game_projects_and_practic\\project_1_3_alien_invasion_full_game\\high_score.json'

        #настройки шрифта для вывода счета
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_images()

    def prep_images(self):
        """Подготовка исходного изображения"""
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Преобразует текущий счет в графическое изображение"""
        rounded_score = round(self.stats.score, -1) #округление числа на заданное число знаков, 
        #заданного во 2 аргументе. Если второй аргумент отрицательный, то функция округляет число
        #до ближайших десятков, сотен, тысяч и т.д. (в нашем случае округление производится до
        #десятков)

        score_str = "{:,}".format(rounded_score) #вставляем запятые при преобразовании числового
        #значения в строку 

        self.score_image = self.font.render(score_str, True, 
            self.text_color, self.settings.bg_color)

        #вывод счета в правой верхней части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Преобразует рекордный счет в графическое изображение"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_color, self.settings.bg_color)

        #рекорд выравнивается по центру верхнего края
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx #выравнивание по оХ
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Проверяет, появилися ли новый рекорд"""
        if self.stats.score > self.stats.high_score:
            self.load_new_high_score()
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def load_new_high_score(self):
        with open(self.filename, 'w') as f:
            json.dump(self.stats.score, f)

    def prep_level(self):
        """Преобразует уровень в графичкеское изображение"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, 
            self.text_color, self.settings.bg_color)

        #уровень выводится аод текущем счетом
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """"Сообщает количество оставшихся кораблей"""
        self.ships = pygame.sprite.Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number *ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Выводит очки, уровень и количество кораблей на экран"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)