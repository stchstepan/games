import sys
import pygame
from alien_invasion_practica_3_space_ship import SpaceShip
from alien_invasion_practic_3_bullet import Bullet

class Practic3:
    """Класс для управления ресусами и поведением игры"""
    def __init__(self):
        """Иницифализирует игру и создает игровые ресурсы"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Pracric 3")
        self.bg_color = (11, 11, 69)

        self.space_ship = SpaceShip(self)
        
        self.bullets = pygame.sprite.Group()

    def run_practic3(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            self.space_ship.update()
            self._update_bullets()
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
        if event.key == pygame.K_UP:
            self.space_ship.moving_up = True

        elif event.key == pygame.K_DOWN:
            self.space_ship.moving_down = True
        
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
            
    def _check_key_up(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_UP:
            self.space_ship.moving_up = False

        elif event.key == pygame.K_DOWN:
            self.space_ship.moving_down = False

    def _fire_bullets(self):
        """Создание нового снаряда и включение его в группу bullets"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.right > self.screen_rect.right:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.bg_color)
        self.space_ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

if __name__ == '__main__':
    practic = Practic3()
    practic.run_practic3()