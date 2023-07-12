import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """Класс для управления звездой"""
    def __init__(self, practic_game_3):
        """Инициализирует звезду и задает ее начальное положение"""
        super().__init__()
        self.screen = practic_game_3.screen

        self.image = pygame.image.load('learning_python_erik_matiz\\part_2\\project1_game\\game_projects_and_practic\\practic_and_other_projects\\images_practic\\zvezda.bmp')
        self.image = pygame.transform.scale(self.image, (70, 66))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        