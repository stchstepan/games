import sys
import pygame
from alien_invasion_practica_2_space_ship import SpaceShip

class Practic2:
    """Класс для управления ресусами и поведением игры"""
    def __init__(self):
        """Иницифализирует игру и создает игровые ресурсы"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Pracric 2")
        self.bg_color = (11, 11, 69)
        
        self.space_ship = SpaceShip(self)

    def run_practic2(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            self.space_ship.update()
            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатия клавиш"""
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_key_down(event)

            elif event.type == pygame.KEYUP:
                self._check_key_up(event)

    def _check_key_down(self, event):
        """Реагирует на нажатие клавиш"""
        if event.key == pygame.K_LEFT:
            self.space_ship.moving_left = True

        elif event.key == pygame.K_RIGHT:
            self.space_ship.moving_right = True
                    
        elif event.key == pygame.K_UP:
            self.space_ship.moving_up = True

        elif event.key == pygame.K_DOWN:
            self.space_ship.moving_down = True

    def _check_key_up(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_LEFT:
            self.space_ship.moving_left = False

        elif event.key == pygame.K_RIGHT:
            self.space_ship.moving_right = False
                    
        elif event.key == pygame.K_UP:
            self.space_ship.moving_up = False

        elif event.key == pygame.K_DOWN:
            self.space_ship.moving_down = False

    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.bg_color)
        self.space_ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    practic = Practic2()
    practic.run_practic2()