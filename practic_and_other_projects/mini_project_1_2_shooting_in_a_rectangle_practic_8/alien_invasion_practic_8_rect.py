import pygame

class Rect:
    """Класс для управления прямоугольником"""

    def __init__(self, ai_practic):
        """Инициализирует прямоугольник и задает его начальную позицию"""
        self.screen = ai_practic.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_practic.settings
        self.color = self.settings.rect_color
        self.rect = pygame.Rect(0, 0, self.settings.rect_width, 
            self.settings.rect_height)
        self.rect.midright = self.screen_rect.midright

        self.y = float(self.rect.y)

    def check_edges(self):
        """Проверка положения прямоугольника"""
        if self.rect.top < self.screen_rect.top or self.rect.bottom > self.screen_rect.bottom:
            return True

    def update(self):
        """Обновляет позицию прямоугольника"""
        self.y += (self.settings.rect_speed_factor * 
            self.settings.change_direction)
        self.rect.y = self.y

    def center_rect(self):
        """Размещает прямоугольника в центре правой стороны"""
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)

    def draw_rect(self):
        pygame.draw.rect(self.screen, self.color, self.rect)