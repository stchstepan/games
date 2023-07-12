import pygame.font

class ButtonMedium():
    def __init__(self, ai_game, msg):
        """Инициализирует атрибуты кнопки"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings 

        #назначение размеров и свойств кнопок
        self.width, self.height = 200, 50
        self.button_color = (255, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48) #используем шрифт по умолчанию

        #построенин объект rect кнопки и выравнивания по центру экрана
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.rect.center = self.screen_rect.center

        #сообщение кнопки создается только один раз
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру"""
        self.msg_image = self.font.render(msg, True, self.text_color, 
            self.button_color) #преобразует текст, хранящийся в msg в 
            #изображение и сохраняется в self.msg_image. 
            #msg - передаем текст, True - сглаживание текста, 
            #self.text_color - цвет текста, self.button_color - 
            #цвет фона текста (в нашем случае цвет фона совпадает с 
            #цветом кнопки. Если цвет фона не указан, то Pygame пытается
            #подобрать прозрачный фон)
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