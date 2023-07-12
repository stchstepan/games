import pygame

class SpiderMan():
    """Класс для управления человеком-пауком.
    Человек-паук и экран отслеживаются как прямоугольный объект."""

    def __init__(self, practic_game): #получает ссылку self и экземпляр класса Practic. 
        """Инициализирует ч-п и задает его начальную позицию"""
        #Получает доступ ко всем игровым ресурсам класса Practic.
        
        self.screen = practic_game.screen #присваеваем экрану, на котором будет находиться изображение
        #настройки экрана (которык хранятся в переменной SCREEN) текущего экземпляра класса Practic
        
        self.screen_rect = practic_game.screen.get_rect() #позволяет разместить картинку в нужной позиции
        #задаем ЭКРАН как прямоуголник

        #зашружает изображение (1 строчка) и получает прямоугольник ИЗОБРАЖЕНИЯ (2 строчка)
        self.image = pygame.image.load('learning_python_erik_matiz\\part_2\\project1_game\\game_projects_and_practic\\practic_and_other_projects\\images_practic\\spider_man.bmp')
        self.image = pygame.transform.scale(self.image, (62, 61)) #уменьшаем изображение до необходимых масштабов
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom #прямоугольник, в котором находится отцентрованное 
        #(midbottom) ИЗОБРАЖЕНИЕ = прямоугольник ЭКРАНА центрирует изображение в прямоугольнике относительно себя

    def blitme(self):
        """Отрисовка человека-паука"""
        #рисует корабль в текущей позиции
        self.screen.blit(self.image, self.rect) #в функцию для построение (blit) передаем два параметра:
        #1 - изображение, которое отрисовываем, 2 - его координаты относительно экрана 