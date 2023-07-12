import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Класс для управления кораблем.
    Корабль и экран отслеживаются как прямоугольный объект."""

    def __init__(self, ai_game): #получает ссылку self и экземпляр класса AlienInvasion. 
        #Получает доступ ко всем игровым ресурсам класса AlienInvasion.
        """Инициализирует корабль и задает его начальную позицию"""
        super().__init__()

        self.screen = ai_game.screen #присваеваем экрану, на котором будет находиться изображение,
        #настройки экрана (которык хранятся в переменной SCREEN) текущего экземпляра класса AlienInvasion

        self.settings = ai_game.settings #создается атрибут settings (экземпляр класса Settings, 
        #используемый в текущем экземпляре класса AlienInvasion)
        
        self.screen_rect = ai_game.screen.get_rect() #позволяет разместить картинку в нужной позиции
        #задаем ЭКРАН как прямоуголник


        #зашружает изображение корабля (1 строчка) и получает прямоугольник для корабля (2 строчка)
        self.image = pygame.image.load('learning_python_erik_matiz\\part_2\\project1_game\\game_projects_and_practic\\project_1_3_alien_invasion_full_game\\images\\ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom #прямоугольник, в котором находится отцентрованное 
        #(midbottom) ИЗОБРАЖЕНИЕ = прямоугольник ЭКРАНА центрирует изображение в прямоугольнике относительно себя

        self.x = float(self.rect.x) #сохраняет вещественные (целые) координаты ЦЕНТРА прямоугольника корабля. Для 
        #точного хранения позиции корабля создается новая переменная, способная хранить дробные значения

        self.moving_right = False #флаг, необходимый для отслеживания неприрывного перемещения корабля при 
        #зажатой клавише ->. По умолчанию этот флаг равен False, так как мы еще не нажали клавишу

        self.moving_left = False #флаг, необходимый для отслеживания неприрывного перемещения корабля при 
        #зажатой клавише <-. По умолчанию этот флаг равен False, так как мы еще не нажали клавишу

    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        if self.moving_right and self.rect.right < self.screen_rect.right: #если были замечены изменения в 
            #переменной moving_right и (координата правого края прямоугольника, в котором хранится корабль (self.rect)
            #меньше значения self.screen_rect.right правого угла прямоугольника, созданного для описания экрана 
            #=> корабль еще не достиг правого края экрана):

            #self.rect.x += 1 #к положению прямоугольника, в котором находится изображение корабля прибавляется
            #1 по оси Х (обновялет атрибуты rect - прямоугольника, описывающего корабль)

            self.x += self.settings.ship_speed_factor #обновляет атрибуты x, не rect, т.к rect сохраняет только целую часть
            #дробного значения. После нажатия изменяет велечину self.x на величину, хранящуюся в экземпляре
            #класса Settings в атрибуте ship_speed_factor

        if self.moving_left and self.rect.left > 0: #если были замечены изменения в переменной moving_left: (если бы мы записали
            #это выражение через elif, то выражение с if всегда имело бы приоритет и при одновременном нажатии
            #двух клавиш, корабль бы не оставался на месте, а двигался бы в приоритетном направлении, то есть 
            #вправо) и (координата левого края прямоугольника, в котором хранится корабль (self.rect)
            #больше 0 (0, т.к. в PyGame отсчет координат начинается с левого нижнего угла) 
            #=> корабль еще не достиг левого края экрана):

            #self.rect.x -= 1 #от положения прямоугольника, в котором находится изображение корабля отниается
            #1 по оси Х (обновялет атрибуты rect - прямоугольника, описывающего корабль)

            self.x -= self.settings.ship_speed_factor #обновляет атрибуты x, не rect, т.к rect сохраняет только целую часть
            #дробного значения. После нажатия изменяет велечину self.x на минус величину, хранящуюся в экземпляре
            #класса Settings в атрибуте ship_speed_factor

        self.rect.x = self.x #после обновления self.x присваевается значение self.x прямоугольнику, хранящем 
        #в себе прямоугольник, описывающий корабль 

    def blitme(self):
        """Отрисовывает корабль"""
        #рисует корабль в текущей позиции
        self.screen.blit(self.image, self.rect) #в функцию для построение (blit) передаем два параметра:
        #1 - изображение, которое отрисовываем, 2 - его координаты относительно экрана 
    
    def center_ship(self):
        """Размещает корабль в центре нижней стороны"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)