import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс, представлющий одного пришельца"""
    def __init__(self, ai_practic):
        """Инициализирует пришельца и задает его начальную позию"""
        super().__init__()
        self.screen = ai_practic.screen
        self.settings = ai_practic.settings

        #загрузка изображения пришельца и назначение атрибута rect
        self.image = pygame.image.load('learning_python_erik_matiz\\part_2\\project1_game\\game_projects_and_practic\\practic_and_other_projects\\images_practic\\new_ai_practic.bmp')
        self.image = pygame.transform.scale(self.image, (68, 47))
        self.rect = self.image.get_rect()

        #каждый новый пришелец появляется в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #сохранение точной горизонтальной позиции пришельца 
        self.x = float(self.rect.x) #нас интрересует горизонтальная скорость, поэтому
        #мы отслеживаем именно ее