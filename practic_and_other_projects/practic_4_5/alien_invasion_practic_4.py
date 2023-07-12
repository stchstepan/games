import sys
import pygame
from alien_invasion_practic_4_star import Star

class Practic4:
    """Класс для управления ресусами и поведением игры"""
    def __init__(self):
        """Иницифализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        
        self.stars = pygame.sprite.Group()
        self._star()

    def run_practic4(self):
        """Запуск основного цикла игры"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.update_screen()

    def _star(self):
        """Создание звезд"""
        star = Star(self)
        star_width, star_height = star.rect.size
        
        available_space_x = self.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)

        available_space_y = self.screen_height - (2 * star_height)
        number_rows = available_space_y // (2 * star_height)

        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)
                
    def _create_star(self, star_number, row_number):
        """Создание звзезды и размещение ее в ряду"""
        star = Star(self)

        star_width = star.rect.width

        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x

        star.rect.y = star.rect.height + 2 * star.rect.height * row_number

        self.stars.add(star)

    def update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    practic3 = Practic4()
    practic3.run_practic4()