import sys
import pygame
from random import randint
from time import sleep

from new_0_settings import Settings
from new_1_ship import Ship
from new_bullet_2 import Bullet
from new_alien_4 import Alien
from new_game_stats_5 import GameStats
from play_button_6 import ButtonPlay
from scoreboard_7 import Scoreboard

class NewAIPractic:
    """Класс для управления ресусами и поведением игры"""

    def __init__(self):
        """Иницифализирует игру и создает игровые ресурсы"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, 
            self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("New Alien Invasion Practic")

        self.play_button = ButtonPlay(self, "Play")
        
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)           
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._create_fleet()

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
                self._check_buttons(mouse_pos)

    def _start_game(self):
        """Начало игры"""
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()

        self.aliens.empty()
        self.bullets.empty()

        self._create_fleet()
        self.ship.center_ship()

        pygame.mouse.set_visible(False)
    
    def _check_buttons(self, mouse_pos):
        """Запускает новую игру при нажатии на кнопку"""
        button_play_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_play_clicked and not self.stats.game_active:
            self._prep_images()
            self._start_game()

    def _prep_images(self):
        """Подготовка исходного изображения"""
        self.settings.initialize_dynamic_settings()
        self._start_game()
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

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

        for bullet in self.bullets.copy():
            if bullet.rect.right > self.screen_rect.right:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Обработка коллизий снарядов с пришельцами"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        if collisions:
            self._scoring(collisions)

        if not self.aliens:
            self._start_new_level()

    def _scoring(self, collisions):
        """Начисляет очки и воспроизводит звук"""
        for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
        #self.score_sound.set_volume(0.4)
        #self.score_sound.play()
        self.sb.prep_score()
        self.sb.check_high_score()

    def _start_new_level(self):
        """Начинает новый уровень"""
        self.bullets.empty()

        self.settings.alien_number = 10

        self._create_fleet()

        self.stats.level += 1
        self.sb.prep_level()

    def _ship_hit(self):
        """Обрабатывает столкновение корабля с пришельцем"""
        if self.stats.ships_left > 0:

            self.stats.ships_left -= 1
            self.sb.prep_ships()

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True) 

    def _update_aliens(self):
        """Обновляет позиции всех пришельцев в флоте"""
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.stats.level -= 1
            self._ship_hit()
        
    def _create_fleet(self):
        """Создание флота вторжения"""
        if self.settings.alien_number <= 10:
            for i in range(self.settings.alien_number):
                alien = Alien(self)
                ox = self.settings.screen_width - i * self.settings.screen_width // self.settings.alien_number
                oy = randint(0, 750)
                alien.rect.x = ox
                alien.rect.y = oy
                self.aliens.add(alien)
                self.settings.alien_number -= 1
            self._move_aliens()

    def _move_aliens(self):
        """Передвижение флота по экрану"""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.alien_speed_factor
            if alien.rect.right <= 0:
                alien.rect.x = 1200
                alien.rect.y = randint(0, 750)

    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.blit(self.settings.bg_color, self.settings.bg_color_rect)

        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        
        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()
        
        pygame.display.flip()

if __name__ == '__main__':
    practic = NewAIPractic()
    practic.run_game()