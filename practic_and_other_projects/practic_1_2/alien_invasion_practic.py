import pygame
import sys
from alien_invasion_practic_spider_man import SpiderMan

class Practic():
    """Класс для управления ресусами и поведением игры"""

    def __init__(self):
        """Иницифализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.width = 1200
        self.high = 800
        self.bg_color = (0, 0, 255)
        self.screen = pygame.display.set_mode((self.width, self.high)) #мы пишеми pygame.display.set_mode...,
        #так как мы сперва обращаемся к модулю pygame, а потом потом к методу display, 
        #который включает в себя еще один метод set_mode

        pygame.display.set_caption("Spider-Man") #задаем имя окну, в котором запускакется игра
        
        self.spider_man = SpiderMan(self) #создаем экземпляр класса загруженного изображения, в который
        #передаются все настройки экрана (self) данного класса (Pracrtic)

    def run_practic(self):
        """Запуск основного цикла игры"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color) # заливаем экран тут потому, что нам нужно, 
            #чтобы он заливался не во время создания экрана игры, а после инициализации (так как при инициализации 
            #мы его только создаем), так как это необходимо потому что по умолчанию экран создается черным 
            #(из-за его инициализации)
            #также, мы не пишем снова pygame.display... так как мы передаем сразу переменную screen
            #ДАННАЯ ПЕРЕМЕННАЯ ЯВЛЯЕТСЯ РАБОЧЕЙ ПОВЕРХНОСТЬЮ (Surface - класс PyGame) ОБРАЩЕИЕ К ДАННОМУ МЕТОДУ
            #В ОБШЕМ ВИДЕ ВЫГЛЯДИТ ТАК pygame.Surface.fill, где Surface - это наш экран
            #в которую уже включены все эти функции. мы лишь добавляем метод fill, для того, чтобы 
            #выполнялась заливка
            
            self.spider_man.blitme() #для экземпляра класса SpderMan вызываем метод, отрисовывающий картинку
            
            pygame.display.flip() # без этой функции экран не будет обновляться => не будет происходить заливка   

if __name__ == '__main__':
    practic = Practic()
    practic.run_practic()