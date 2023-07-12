import sys
import pygame

class Practic2_3:
    """Класс для управления ресусами и поведением игры"""

    def __init__(self):
        """Иницифализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))

    def run_practic_2_3(self):
        """Запуск основного цикла игры"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    print(event.key)

if __name__ == '__main__':
    test = Practic2_3()
    test.run_practic_2_3()