import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс, представлющий одного пришельца"""
    def __init__(self, ai_game):
        """Инициализирует пришельца и задает его начальную позию"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #загрузка изображения пришельца и назначение атрибута rect
        self.image = pygame.image.load('learning_python_erik_matiz\\part_2\\project1_game\\game_projects_and_practic\\project_1_3_alien_invasion_full_game\\images\\alien.bmp')
        self.rect = self.image.get_rect()

        #каждый новый пришелец появляется в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #сохранение точной горизонтальной позиции пришельца 
        self.x = float(self.rect.x) #нас интрересует горизонтальная скорость, поэтому
        #мы отслеживаем именно ее

    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Перемещает пришельцев влево и право"""
        self.x += (self.settings.alien_speed_factor * 
            self.settings.fleet_direction)
        self.rect.x = self.x