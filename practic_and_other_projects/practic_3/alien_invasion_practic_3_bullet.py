import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления снарядами, выпущенными кораблем"""

    def __init__(self, ai_practic_3):
        """Создает объект снарядов в текущей позиции корабля"""
        super().__init__()
        self.screen = ai_practic_3.screen
        self.color = (255, 200, 255)
        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.midright = ai_practic_3.space_ship.rect.midright
        self.x = float(self.rect.x)

    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Перемещает снаряд вверх по экрану"""
        self.x += 1
        self.rect.x = self.x

    def draw_bullet(self):
        """Выводит снаряд на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)