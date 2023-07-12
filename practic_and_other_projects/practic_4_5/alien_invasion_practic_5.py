import sys
import pygame
from alien_invasion_practic_5_rain import Drop

class Practic5():
    """Класс для управления ресусами и поведением"""

    def __init__(self):
        """Иницифализирует и создает игровые ресурсы"""
        pygame.__init__
        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.bg_color = (0, 0, 0)

        pygame.display.set_caption("Practic 5")

        self.rains = pygame.sprite.Group()

        self._create_drop()

    def run_practic_5(self):
        """Запуск основного цикла игры"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._update_raindrops()
            self.update_screen()

    def _create_drop(self):
        """Создание капель (сколько штук)"""
        drop = Drop(self)
        drop_width, drop_height = drop.rect.size

        available_space_x = self.screen_width - drop_width
        self.number_drop_x = available_space_x // (2* drop_width)

        available_space_y = self.screen_height
        number_rows = available_space_y // (2 * drop_height)

        for row_number in range(number_rows):
            self._create_row(row_number)

    def _create_row(self, row_number):
        """Создание капли и размещение ее в ряду"""
        for drop_number in range(self.number_drop_x):
            self._create_drops(drop_number, row_number)

    def _create_drops(self, drop_number, row_number):
        """Создание капель"""
        drop = Drop(self)
        drop_width, drop_height = drop.rect.size

        drop.x = drop_width + 2 * drop_width * drop_number

        drop.y = 2 * drop.rect.height * row_number
        drop.rect.y = drop.y

        self.rains.add(drop)

    def _update_raindrops(self):
        """Обновление положения капель"""
        self.rains.update()

        make_new_drops = False
        for drop in self.rains.copy():
            if drop.check_disappeared():
                self.rains.remove(drop)
                make_new_drops = True
                
        if make_new_drops:
            self._create_row(0)


    def update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.bg_color)
        self.rains.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    run_pracric = Practic5()
    run_pracric.run_practic_5()