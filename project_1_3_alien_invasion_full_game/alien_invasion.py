#TO EXIT ENTER 'Q'

import sys
import pygame
from time import sleep
import random

from settings import Settings
from ship import Ship
from bullet import Bullet, AlienBullet
from alien import Alien
from game_stats import GameStats
from easy_button import ButtonEasy
from meduim_button import ButtonMedium
from hard_button import ButtonHard
from scoreboard import Scoreboard

class AlienInvasion:
    """Класс для управления ресусами и поведением игры"""

    def __init__(self): 
        """Иницифализирует игру и создает игровые ресурсы"""
        pygame.init() #инициализируем все функции PyGame

        self.settings = Settings() #создаем экземпляр класса Settings и сохраняем его в переменной settings

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #вводим возможность открывать игру в 
        #полный экран. В pygame.display.set_mode((0, 0), pygame.FULLSCREEN) сперва передаем (0, 0), а потом
        #pygame.FULLSCREEN, т.к. эти значения приказывают PyGame вычислить параметры экрана

        self.settings.screen_width = self.screen.get_rect().width #self.screen.get_rect().width используется 
        #для обновления параметра ширины экрана screen_width экземпляра settings класса Settings (который 
        #записан в self.settings.screen_width). 

        self.settings.screen_height = self.screen.get_rect().height #self.screen.get_rect().height используется 
        #для обновления параметра высоты экрана screen_height экземпляра settings класса Settings (который 
        #записан в self.settings.screen_height).

        #self.screen = pygame.display.set_mode(
            #(self.settings.screen_width, self.settings.screen_height)) #мы пишеми pygame.display.set_mode...,
        #так как мы сперва обращаемся к модулю pygame, а потом потом к методу display, 
        #который включает в себя еще один метод set_mode (так как настройки хранятся в переменной settings,
        #то мы передаем их оттуда)

        pygame.display.set_caption("Alien Invasion") #задаем имя окну, в котором запускакется игра
 
        self.stats = GameStats(self) #создание экземпляра для хранения игровой статистики

        self.sb = Scoreboard(self) #создание экземпляра для хранения игровых результатов

        self.ship = Ship(self) #создаем экземпляр класса загруженного изображения, в который
        #передаются все настройки экрана (self) данного класса (AlienInvasion)

        self.bullets = pygame.sprite.Group() #группа для хранения всех летящиx снарядов, чтобы программа
        #могла управлять их полетом. pygame.sprite.Group() - своего рода список, с расширенными возможностями 
        #Мы воспользуемся группой для прорисовки снарядов на экране при каждом проходе основного цикла и
        #обновления текущей позиции каждого снаряда

        self.aliens_bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group() #группа для хранения всех НЛО, чтобы программа могла управлять 
        #их полетом и появлением.

        self._create_fleet()

        self.easy_button = ButtonEasy(self, "Easy") #создание кнопки Easy

        self.medium_button = ButtonMedium(self, "Medium") #создание кнопки Medium

        self.hard_button = ButtonHard(self, "Hard") #создание кнопки Hard

        self.fire_sound = pygame.mixer.Sound('learning_python_erik_matiz\\part_2\\project1_game\\game_projects_and_practic\\project_1_3_alien_invasion_full_game\\sounds\\mixkit-electronic-retro-block-hit-2185.wav')
        
        self.button_sound = pygame.mixer.Sound('learning_python_erik_matiz\\part_2\\project1_game\\game_projects_and_practic\\project_1_3_alien_invasion_full_game\\sounds\\button-124476.mp3')

        self.score_sound = pygame.mixer.Sound('learning_python_erik_matiz\\part_2\\project1_game\\game_projects_and_practic\\project_1_3_alien_invasion_full_game\\sounds\\coin_c_02-102844.mp3')

        self.ship_hit_sound = pygame.mixer.Sound('learning_python_erik_matiz\\part_2\\project1_game\\game_projects_and_practic\\project_1_3_alien_invasion_full_game\\sounds\\mixkit-arcade-retro-game-over-213.wav')

        self.game_over_sound = pygame.mixer.Sound('learning_python_erik_matiz\\part_2\\project1_game\\game_projects_and_practic\\project_1_3_alien_invasion_full_game\\sounds\\dead-8bit-41400.mp3')

        pygame.mixer.music.load('learning_python_erik_matiz\\part_2\\project1_game\\game_projects_and_practic\\project_1_3_alien_invasion_full_game\\sounds\\8bit-music-for-game-68698.mp3')

        pygame.mixer.music.set_volume(0.5)

        pygame.mixer.music.play(-1)

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events() #проверяем события

            if self.stats.game_active: #действия, которые должны выполняться только при активной игре

                self.ship.update() #метод .update обновляет не весь экран, а лишь его часть (в данном случае
                #ship)

                self._update_bullets() #обновляет информацию о снарядах

                self._update_bullets_aliens() #обновляет информацию о снарядах НЛО

                self._random_shooting() #шанс выстрела НЛО

                self._update_aliens() #метод для управления передвижением флота

            self._update_screen() #обновляем экран

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши"""
        for event in pygame.event.get(): #каждый раз, когда пользователь нажимает клавишу на клавиатуре/мыше
            #это нажатие регестрируется в PyGame как событие. Кждое событие идентифицируется методом
            #pygame.event.get().

                if event.type == pygame.QUIT:
                    sys.exit() #выход при нажатии крестика

                elif event.type == pygame.KEYDOWN: #нажатие на клавиатуре регестрируется как событие KEYDOWN

                    self._check_keydown_events(event) #после рефакторинга перенесли в отдельный метод
                    #(_check_keydown_events) дейтсвия, отвечающие за передвижение корабля при нажатии клавиш

                elif event.type == pygame.KEYUP: #отпускание клавишы на клавиатуре регестрируется как событие KEYUP

                    self._check_keyup_events(event) #после рефакторинга перенесли в отдельный метод
                    #(_check_keyup_events) дейтсвия, отвечающие за передвижение корабля при отпускание клавиш

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos() #обнаруживает клик мышки в любой точке экрана
                    self._check_buttons(mouse_pos)

    def _start_game(self):
        """Начало игры"""
        #сброс игровой статистики
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score() #обнуление счета

        #очистка списков пришельцев и снарядов
        self.aliens.empty()
        self.bullets.empty()

        #создание нового флота и размещение корабля в центре
        self._create_fleet()
        self.ship.center_ship()

        #указатель мыши скрывается
        pygame.mouse.set_visible(False)
    
    def _check_buttons(self, mouse_pos):
        """Запускает новую игру при нажатии на кнопку"""
        button_clicked_easy = self.easy_button.rect.collidepoint(mouse_pos) #флаг Easy
        button_clicked_medium = self.medium_button.rect.collidepoint(mouse_pos) #флаг Medium
        button_clicked_hard = self.hard_button.rect.collidepoint(mouse_pos) #флаг Hard

        if button_clicked_easy and not self.stats.game_active:
            self.button_sound.set_volume(0.5)
            self.button_sound.play()
            self._run_easy_game()

        elif button_clicked_medium and not self.stats.game_active:
            self.button_sound.set_volume(0.5)
            self.button_sound.play()
            self._run_medium_game()

        elif button_clicked_hard and not self.stats.game_active:
            self.button_sound.set_volume(0.5)
            self.button_sound.play()
            self._run_hard_game()

    def _prep_images(self):
        """Подготовка исходного изображения"""
        self.settings.initialize_dynamic_settings() #сброс настроек при новой игре
        self._start_game() 
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

    def _run_easy_game(self):
        """Запускает легкую игру"""
        pygame.mixer.music.unpause()
        self._prep_images()

    def _run_medium_game(self):
        """Запускает среднюю игру"""
        pygame.mixer.music.unpause()
        self.settings.speedup_scale = 1.2
        self.settings.ship_speed_factor = 2.0
        self.settings.bullet_speed_factor = 3.5
        self.settings.alien_speed_factor = 1.5
        self._prep_images()

    def _run_hard_game(self):
        """Запускает сложную игру"""
        pygame.mixer.music.unpause()
        self.settings.speedup_scale = 1.3
        self.settings.ship_speed_factor = 2.5
        self.settings.bullet_speed_factor = 4.0
        self.settings.alien_speed_factor = 2.0
        self._prep_images()

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш"""
        if event.key == pygame.K_RIGHT: #если событие key == ->, то:
            #self.ship.rect.x += 1 #переместить корабль вправо на 1 (1.5) пиксель (т.к корабль находится в
            #в переменной ship и является переменной класса Ship, в котором есть переменная rect,
            #отвечающая за квадрат, описывающий изображение корабля, то для обращения к этому 
            #квадрату мы используем точечную запись self.ship.rect.x, где self - это ссылка на 
            #переменную текущего экземпляра, а x - это указание, что нам нужно сдвинуться на n
            #(в нашем случае 1 (1.5)) пикселей вправо по оси X)

            self.ship.moving_right = True #когда клавиша -> зажата - мы присваеваем переменной
            #moving_right экземпляра ship класса Ship значение True => получаем непрерывное перемещение
            #корабля вправо

        elif event.key == pygame.K_LEFT: #то же самое, что и для правой клавиши

            self.ship.moving_left = True #то же самое, что и для правой клавиши

        elif event.key == pygame.K_q: #если нажата клавиша q:

            sys.exit() #выполняется выход из игры

        elif event.key == pygame.K_p and not self.stats.game_active:
            self._start_game()
        
        elif event.key == pygame.K_SPACE: #если нажимается пробел, то появялются снаряды
            self._fire_bullet() #метод для вызова снарядов (их отрисовки)

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT: #если событие key == ->, то:

            self.ship.moving_right = False #когда клавиша -> отпушена - мы присваеваем переменной
            #moving_right экземпляра ship класса Ship значение False => прекращаем движение

        elif event.key == pygame.K_LEFT: #то же самое, что и для правой клавиши

            self.ship.moving_left = False #то же самое, что и для правой клавиши

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets"""
        if len(self.bullets) < self.settings.bullets_allowed: #позволяет выпускать новые пули тоько в том 
            #случае, если кол-во пуль, находящихся на экране не более заданного в настройках
        
            new_bullet = Bullet(self) #создаем экземпляр класса Bullet

            self.bullets.add(new_bullet) #добавляем этот экземпляр в группу
            
            self.fire_sound.set_volume(0.2)

            self.fire_sound.play()

    def _random_shooting(self):
        """Шанс выстрела пули НЛО"""
        if random.randint(0, 70) == 1: #если случайное число = 1, то НЛО стреляет
            self._alien_shoot()

    def _alien_shoot(self):
        """Создание нового снаряда и включение его в группу aliens_bullets"""
        if len(self.aliens_bullets) < self.settings.bullets_allowed_aliens:
            new_bullet = AlienBullet(self)
            self.aliens_bullets.add(new_bullet)
            self.fire_sound.set_volume(0.2)
            self.fire_sound.play()

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды"""
        self.bullets.update() #обновление позиции пули

        #удаление снарядов, выпушедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions() #вызов функции, проверяющую коллизию

    def _update_bullets_aliens(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды (для НЛО)"""
        self.aliens_bullets.update()
        screen_rect = self.screen.get_rect()

        for bullet in self.aliens_bullets.copy():
            if bullet.rect.top >= screen_rect.bottom:
                self.aliens_bullets.remove(bullet)

        self._check_bullet_ship_collisions()

    def _check_bullet_alien_collisions(self):
        """Обработка коллизий снарядов с пришельцами"""
        #проверка попаданий в пришельцев
        #при обноружении попадания удалить снаряд и пришельца

        collisions = pygame.sprite.groupcollide( #метод sprite.groupcollide() сравнивает прямоугольник rect каждого
        #элемента другой группы. В данном случае он сравнивает прямоугольник каждого снаряда с прямоугольником 
        #каждого пришельца и возвращает словарь со снарядами и пришельцами, между которыми обноружены коллизии.
        #Каждый ключ в словаре представляет снаряд, а ассоцируемое с ним значение - пришельца, в которого попал снаряд.

            self.bullets, self.aliens, True, True) #сначала перебираем все снаряды в self.bullets, а затем перебирает
            #всех пришельцев в self.aliens. Каждый раз, когда между прямоугольником снаряда и пришельца образовывается 
            #перекрытие, groupcollide() добавляет пару ключ-значение в возвращаемый словарь. Два аргумента True сообщают
            #Pygame, нужно ли удалять столкнувшиеся объекты: снаряд и пришельца. Первое True - для пули, второе - для
            #пришельца.
            #[ЧТОБЫ СОЗДАТЬ СВЕРХМОЩНЫЙ СНАРЯД, КОТОРЫЙ БУДЕТ УНИЧТОЖАТЬ ВСЕХ ПРИШЕЛЬЦЕВ НА СВОЕМ ПУТИ, МОЖНО ПЕРЕДАТЬ 
            #В ПЕРВОМ АРГУМЕНТЕ False, А ВО ВТОРОМ True]

        if collisions:
            self._scoring(collisions)

        if not self.aliens: #проверяем, пуста ли группа aliens
            self._start_new_level()

    def _check_bullet_ship_collisions(self):
        """Обработка коллизий снарядов с кораблем"""
        for bullet in self.aliens_bullets.sprites():
            if bullet.rect.colliderect(self.ship.rect):
                self._ship_hit()

    def _scoring(self, collisions):
        """Начисляет очки и воспроизводит звук"""
        for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
        self.score_sound.set_volume(0.4)
        self.score_sound.play()
        self.sb.prep_score()
        self.sb.check_high_score() #каждый раз при попадании сравниваем текущий результат с рекордом

    def _start_new_level(self):
        """Начинает новый уровень"""
        #уничтожение существующих снарядов и создание нового флота

        self.bullets.empty() #если группа пуста, то все снаряды убираются методом empty

        self._create_fleet() #снова заполняем экран пришельцами

        self.settings.increase_speed() #увеличиваем сложность игры

        #увелечение отображаемого уровня
        self.stats.level += 1
        self.sb.prep_level()

    def _ship_hit(self):
        """Обрабатывает столкновение корабля с пришельцем"""
        if self.stats.ships_left > 0:
            
            self.ship_hit_sound.set_volume(0.5)
            self.ship_hit_sound.play()            

            self.stats.ships_left -= 1 #уменьшает ships_left
            self.sb.prep_ships()

            #очистка списка пришельцев и снарядов
            self.aliens.empty()
            self.bullets.empty()

            #создание нового флота и размещение корабля в центре
            self._create_fleet()
            self.ship.center_ship()

            #пауза
            sleep(0.5)
        
        else:
            pygame.mixer.music.pause()
            self.game_over_sound.set_volume(0.5)
            self.game_over_sound.play()
            self.stats.game_active = False #если был потерян последний корабль, то значение флага меняется на False
            pygame.mouse.set_visible(True) #мышка снова появляется, как только игра становится неактивна

    def _update_aliens(self):
        """Обновляет позиции всех пришельцев в флоте"""
        self._check_fleet_edges() #проверяем достигли ли пришельцы края экрана
        self.aliens.update() #обновляет позицию пришельцев в соответсвии с настройками скорости

        #проверка коллизий "пришелец-корабль"
        if pygame.sprite.spritecollideany(self.ship, self.aliens): #функция получает два аргумента, спрайт (1 пришелец) и 
            #группу (пришельцев). Функция пытается найти любой элемент группы, вступивший в коллизию со спрайтом, и 
            #останавливает цикл по группе сразу же после обнаружения столкнувшегося элемента. 
            #В данном случае перебираем группу aliens возвращаем первого пришельца, столкнувшегося с кораблем ship.
            #Если ни одна коллизиия не была одноружена, то spritecollideany возвращает None и блок if не выполняется.

            self._ship_hit() #метод, ведущий статистику жизней игрока

        self._check_aliens_bottom() #проверяет, добрался ли пришелец до нижнего края экрана
    
    def _check_aliens_bottom(self):
        """Проеверяет, добрались ли пришельцы до нижнего края экрана"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #происходит то де самое, что и при столкновении с кораблем
                self._ship_hit()
                break

    def _create_fleet(self):
        """Создание флота вторжения"""
        alien = Alien(self) #создание пришельца. Этот пришелец не включается в группу отрисованных. 
        #В группу включаются лишь те, которые находятся в цикле for. Данный экземпляр класса Aliens
        #нужен для определения ширины одного пришельца, которая используется далее.

        alien_width, alien_height = alien.rect.size #ширина и высота одного НЛО
        
        available_space_x = self.settings.screen_width - (2 * alien_width) #доступное место на экране;
        #вычисляется по формуле: ширина_экрана - 2 * ширина пришельца. То есть по бокам с каждой стороны
        #мы оставляем пространство равное одному пришельцу

        number_aliens_x = available_space_x // (2 * alien_width) #кол-во НЛО, которые могут 
        #поместиться в один ряд на экране; вычисляется по формуле: доступное_место_на_экране // (деление без остатка)
        #2 * ширину НЛО. То есть мы делим доступное пространство на две ширины НЛО, так как между каждым 
        #пришельцем также есть растояние, равное одной ширине пришельца. Делим без остатка, так как нам 
        #необходимо, чтобы на экране помещалось целое кол-во НЛО

        #определяет кол-во рядов, помещающихся на экране
        ship_height = self.ship.rect.height #определяем высоту корабля

        available_space_y = (self.settings.screen_height - 
            3 * (alien_height) - ship_height) #вычисляем свободное место на экаране по вертикале. От собственной высоты 
            #экрана мы вычитаем 3 высоты пришельца (так как высота одного пришельца - это отступ от верхнего края экрана
            #вторая высота - это расстояние между пришельцами, третья высота - отступ от корабля) минус высота корабля
            #(так как нам нужно расстояние от пришельцев)
        
        number_rows = available_space_y // (2 * alien_height) #вычисляем количество рядов. Под каждым рядом должно быть
        #пустое пространство, равное одной высоте пришельца, а так как у нас одна высота пришельца уже есть (который
        #появляется на экране), то нам надо добавить еще одну - расстояние между рядами. Снова используем целочисленное 
        #деление, так как кол-во пришельцев должно быть целым

        #создание флота пришельцев
        for row_number in range(number_rows): #создает один ряд пришельцев
            for alien_number in range(number_aliens_x): #создает от 0 до number_aliens_x кол-ва пришельцев 
                self._create_alien(alien_number, row_number) #вызов вспомогательной функции, отвечающую за создание и размещение 
            #пришельцев
            
    def _create_alien(self, alien_number, row_number):
        """Создание пришельца и размещение его в ряду"""
        alien = Alien(self) #создание пришельца

        alien_width, alien_height = alien.rect.size #ширина и высота одного НЛО

        alien.x = alien_width + 2 * alien_width * alien_number #задаем координату х для нового 
            #пришельца для размещения его в ряду. 

        alien.rect.x = alien.x #положение прямоугольника НЛО = положению пришельца (необходимо), 
        #так как в alien.py мы используем положение прямоугольника для сохранения координат пришельца,
        #а не координаты самого пришельца

        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number #положение прямокгольника НЛО = 
        # = высота прямоугольника НЛО (так как нам нужно создать пустое место у верхнего края экрана) 
        # + две высоты прямоугольника НЛО (так как каждый новы ряд начинается на 2 высоты последнего ряда) * на номер ряда 
        #НЛО (так как ноемр первого ряда = 0, то он остается неизменно на экране, а все осталдьные смещаются вниз в соответствии)
        #со своим номером

        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана"""
        for alien in self.aliens.sprites(): #для всех пришельцев в "спрайте"

            if alien.check_edges(): #если был достигнут край (вернулось True)

                self._change_fleet_direction() #направление движения пришельцев меняется

                break

    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление флота"""
        for alien in self.aliens.sprites(): #для всех пришельцев в "спрайте"

            alien.rect.y += self.settings.fleet_drop_speed #уменьшает выосту каждого из НЛО

        self.settings.fleet_direction *= -1 #меняем на противоположенное значение fleet_direction

    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_color) # заливаем экран тут потому, что нам нужно, 
            #чтобы он заливался не во время создания экрана игры, а после инициализации (так как при инициализации 
            #мы его только создаем), так как это необходимо потому что по умолчанию экран создается черным 
            #(из-за его инициализации)
            #также, мы не пишем снова pygame.display... так как мы передаем сразу переменную screen
            #ДАННАЯ ПЕРЕМЕННАЯ ЯВЛЯЕТСЯ РАБОЧЕЙ ПОВЕРХНОСТЬЮ (Surface - класс PyGame) ОБРАЩЕИЕ К ДАННОМУ МЕТОДУ
            #В ОБШЕМ ВИДЕ ВЫГЛЯДИТ ТАК pygame.Surface.fill, где Surface - это наш экран
            #в которую уже включены все эти функции. мы лишь добавляем метод fill, для того, чтобы 
            #выполнялась заливка (так как настройк в переменной settings, то и передаем их через нее)

        self.ship.blitme() #для экземпляра класса Ship вызываем метод, отрисовывающий картинку

        for bullet in self.bullets.sprites(): #для каждого снаряда в группе со снарядами:
            bullet.draw_bullet() #отрисовать снаряд

        self.aliens.draw(self.screen) #передаем поверхность, на которой будет отрисовываться НЛО

        for bullet in self.aliens_bullets.sprites():
            bullet.draw_bullet()

        self.sb.show_score() #вывод информации о счете

        #кнопка Play отображается в том случае, если игра неактивна
        if not self.stats.game_active:
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.hard_button.draw_button()

        pygame.display.flip() #отображение последнего прорисованного экрана

if __name__ == '__main__':
    #создание экземпляра класса и запуск игры
    ai = AlienInvasion()
    ai.run_game()