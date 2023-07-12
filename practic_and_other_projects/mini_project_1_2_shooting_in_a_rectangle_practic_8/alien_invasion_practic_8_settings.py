class Settings():
    """Класс для хранения всех настроек Alien Invasion"""
    
    def __init__(self):
        """Инициализирует настройки игры"""
        #параметры игры
        self.screen_width = 1200 #ширина экрана в пикселях

        self.screen_height = 800 #высота экрана в пикселях

        self.bg_color = (11, 11, 69) #цвет экрана в RGB

        #настройки корабля

        self.deffend_ships = 0

        #параметры снаряда

        self.bullet_width = 15 #ширина снаряда = 3 пикселя

        self.bullet_height = 3 #высота снаряда = 15 пикселей

        self.bullet_color = (255, 200, 255) #цвет снаряда = темно-синий по RGB

        self.bullets_limit = 3 #кол-во дозволенных промахов в начале игры
        
        #настройки прямоугольника

        self.rect_color = (0, 200, 130)

        self.rect_width = 30

        self.rect_height = 80

        self.change_direction = -1

        #темп ускорения игры

        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed_factor = 1.0 #при перемещении корабля его позиция меняется на 1.5 пикслея
        #а не на 1, но атрибуты прямоугольников (такие, как y) принимают только
        #целые значения, поэтому в модуль ship нужно внести изменения

        self.bullet_speed_factor = 2.0 #скорость снаряда = 1 пиксель

        self.rect_speed_factor = 1.0 #скорость прямоугольника

        #fleet_direction = 1 обозначает движение вправо; а -1 - влево
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed_factor *= self.speedup_scale

        self.bullet_speed_factor *= self.speedup_scale

        self.rect_speed_factor *= self.speedup_scale