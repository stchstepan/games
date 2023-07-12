import pygame

class Settings():
    """Класс для хранения всех настроек Alien Invasion"""
    
    def __init__(self):
        """Инициализирует настройки игры"""
        #параметры игры
        self.screen_width = 1200 #ширина экрана в пикселях

        self.screen_height = 800 #высота экрана в пикселях

        self.bg_color = pygame.image.load('learning_python_erik_matiz\\part_2\\project1_game\\game_projects_and_practic\\practic_and_other_projects\\images_practic\\background_project.bmp') #фон экрана

        self.bg_color = pygame.transform.scale(self.bg_color, (1470, 830))

        self.bg_color_rect = self.bg_color.get_rect()

        self.ship_limit = 3 #кол-во кораблей в начале игры

        #параметры снаряда

        self.bullet_width = 15 #ширина снаряда = 3 пикселя

        self.bullet_height = 3 #высота снаряда = 15 пикселей

        self.bullet_color = (255, 200, 255) #цвет снаряда = темно-синий по RGB

        #настройки пришельцев

        self.alien_number = 10

        self.initialize_dynamic_settings()

        self.ship_speed = 1

    def initialize_dynamic_settings(self):
        """Инициализирует настройки игры"""

        self.bullet_speed_factor = 1.0 #скорость снаряда = 1 пиксель

        self.alien_speed_factor = 1.0 #скорость пришельца

        #подсчет очков
        self.alien_points = 50