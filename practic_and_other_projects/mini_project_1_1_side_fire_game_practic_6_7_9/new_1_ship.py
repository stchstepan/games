import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Класс для управления кораблем.
    Корабль и экран отслеживаются как прямоугольный объект."""

    def __init__(self, ai_practic):
        """Инициализирует корабль и задает его начальную позицию"""
        super().__init__()

        self.screen = ai_practic.screen
        self.settings = ai_practic.settings
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('learning_python_erik_matiz\\part_2\\project1_game\\game_projects_and_practic\\practic_and_other_projects\\images_practic\\practic2_space_ship.bmp')
        self.image = pygame.transform.scale(self.image, (62, 61))
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.x = float(self.rect.x)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= self.settings.ship_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Отрисовывает корабль"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль в центре нижней стороны"""
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)