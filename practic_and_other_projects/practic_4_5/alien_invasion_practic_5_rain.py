import pygame
from pygame.sprite import Sprite

class Drop(Sprite):
    """Класс для управления каплями"""

    def __init__(self, practic_game_5):
        """Создает объект капли"""
        super().__init__()
        self.screen = practic_game_5.screen
        
        self.image = pygame.image.load("learning_python_erik_matiz\\part_2\\project1_game\\game_projects_and_practic\\practic_and_other_projects\\images_practic\\rain.bmp")
        self.image = pygame.transform.scale(self.image, (51, 51))

        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

        self.drops_speed = 1.0

    def check_disappeared(self):
        """Проверка падения капель"""
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False

    def update(self):
        """Перемещает каплю вниз по экрану"""
        self.y += self.drops_speed
        self.rect.y = self.y
