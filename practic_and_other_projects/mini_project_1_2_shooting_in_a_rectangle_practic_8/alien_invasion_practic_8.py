import pygame
import sys
from time import sleep

from alien_invasion_practic_8_settings import Settings
from alien_invasion_practic_8_ship import Ship
from alien_invasion_practic_8_bullet import Bullet
from alien_invasion_practic_8_rect import Rect
from alien_invasion_practic_8_game_stats import GameStats
from alien_invasion_practic_8_button import Button

class Practic8:
    """Класс для управления ресусами и поведением игры"""

    def __init__(self):
        """Иницифализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Practic 8")

        self.stats = GameStats(self)

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

        self.rect = Rect(self)

        self.play_button = Button(self, "Play")

    def run_practic8(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_rect()
            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши"""
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)

            elif event.type == pygame.KEYUP:
                self._check_key_up_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _start_game(self):
        """Начало игры"""
        self.stats.reset_stats()
        self.stats.game_active = True

        self.bullets.empty()

        self.ship.center_ship()

        pygame.mouse.set_visible(False)
    
    def _check_play_button(self, mouse_pos):
        """Запускает новую игру при нажатии на кнопку Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self._start_game()

    def _check_key_down_events(self, event):
        """Реагирует на нажатие клавиш"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True

        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
            
    def _check_key_up_events(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False

        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullets(self):
        """Создание нового снаряда и включение его в группу bullets"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды"""
        self.bullets.update()
        self._check_bullet_rect_collisions()

        for bullet in self.bullets.copy():
            if bullet.rect.right > self.screen_rect.right:
                self.bullets.remove(bullet)

    def _check_bullet_rect_collisions(self):
        """Обработка коллизий снарядов с прямоугольником"""
        for bullet in self.bullets.sprites():
            if bullet.rect.colliderect(self.rect.rect):
                self.rect.center_rect()
                self.bullets.empty()
                sleep(0.5)
                self.settings.increase_speed()

            elif bullet.rect.right > self.screen_rect.right:
                self._check_miss()

    def _check_miss(self):
        """Проверка на промах"""
        if self.stats.bullets_left > 0:
            self.stats.bullets_left -= 1

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_rect(self):
        """Обновление позиции прямоугольника"""
        self._check_rect_edges()
        self.rect.update()

    def _check_rect_edges(self):
        """Проверка положения прямоугольника на экране"""
        if self.rect.check_edges():
            self._change_rect_direction()

    def _change_rect_direction(self):
        """Изменение направления движения прямоугольника"""
        self.settings.change_direction *= -1

    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_color)
        
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.rect.draw_rect()

        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == "__main__":
    practic = Practic8()
    practic.run_practic8()