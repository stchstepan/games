import pygame.font

class ButtonPlay():
    def __init__(self, ai_practic, msg):
        """Инициализирует атрибуты кнопки"""
        self.screen = ai_practic.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_practic.settings 

        #назначение размеров и свойств кнопок
        self.width, self.height = 200, 80
        self.button_color = (111, 0, 172)
        self.text_color = (205, 215, 232)
        self.font = pygame.font.Font('learning_python_erik_matiz\\part_2\\project1_game\\game_projects_and_practic\\practic_and_other_projects\\font_practic\\BACKTO1982.TTF', 48)

        #построенин объект rect кнопки и выравнивания по центру экрана
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.rect.center = self.screen_rect.center

        #сообщение кнопки создается только один раз
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру"""
        self.msg_image = self.font.render(msg, True, self.text_color, 
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Отрисовывает изображение кнопки"""
        #отображение пустой кнопки и вывод сообщения
        self.screen.fill(self.button_color, self.rect) #рисуем прямоугольную часть
        #кнопки

        self.screen.blit(self.msg_image, self.msg_image_rect) #вывдодит изображение
        #текста на экран с передачей изображения и объекта rect, связанного с 
        #изображением