import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления снарядами, выпущенными кораблем"""

    def __init__(self, ai_practic):
        """Создает объект снарядов в текущей позиции корабля"""
        super().__init__()
        self.screen = ai_practic.screen
        self.settings = ai_practic.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midright = ai_practic.ship.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        """Перемещает снаряд вверх по экрану"""
        self.x += self.settings.bullet_speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        """Выводит снаряд на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)