import pygame

class SpaceShip:
    def __init__(self, ai_practic_2):
        """Класс для управления кораблем.
        Корабль и экран отслеживаются как прямоугольный объект."""
        pygame.init()
        self.screen = ai_practic_2.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('learning_python_erik_matiz\\part_2\\project1_game\\game_projects_and_practic\\practic_and_other_projects\\images_practic\\practic2_space_ship.bmp')
        self.image = pygame.transform.scale(self.image, (62, 61))
        self.image_rect = self.image.get_rect()

        self.moving_right = False 
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.image_rect.midbottom = self.screen_rect.midbottom

    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        if self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.image_rect.x += 1

        if self.moving_left and self.image_rect.left > 0:
            self.image_rect.x -= 1
        
        if self.moving_up and self.image_rect.top > self.screen_rect.top:
            self.image_rect.y -= 1
        
        if self.moving_down and self.image_rect.bottom < self.screen_rect.bottom:
            self.image_rect.y += 1

    def blitme(self):
        """Отрисовывает корабль"""
        self.screen.blit(self.image, self.image_rect)