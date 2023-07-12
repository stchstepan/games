class Settings():
    """Класс для хранения всех настроек Alien Invasion"""
    
    def __init__(self):
        """Инициализирует статические настройки игры"""
        #параметры игры
        self.screen_width = 1200 #ширина экрана в пикселях

        self.screen_height = 800 #высота экрана в пикселях

        self.bg_color = (230, 230, 230) #цвет экрана в RGB

        #настройки корабля

        self.ship_limit = 3 #кол-во кораблей в начале игры

        #параметры снаряда

        self.bullet_width = 3 #ширина снаряда = 3 пикселя

        self.bullet_height = 15 #высота снаряда = 15 пикселей

        self.bullet_color = (60, 60, 60) #цвет снаряда = темно-синий по RGB

        self.bullets_allowed = 3 #разрешенное количсество пуль 
        
        #настройки пришельцев

        self.fleet_drop_speed = 10 #величина снижения флота при достижении им края
        
        self.bullets_allowed_aliens = 5

        #темп ускорения игры
        self.speedup_scale = 1.1

        #темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed_factor = 1.5 #при перемещении корабля его позиция меняется на 1.5 пикслея
        #а не на 1, но атрибуты прямоугольников (такие, как х) принимают только
        #целые значения, поэтому в модуль ship нужно внести изменения

        self.bullet_speed_factor = 3.0 #скорость снаряда = 1 пиксель

        self.alien_speed_factor = 1.0 #скорость пришельца

        #fleet_direction = 1 обозначает движение вправо; а -1 - влево
        self.fleet_direction = 1

        #подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельца"""
        self.ship_speed_factor *= self.speedup_scale

        self.bullet_speed_factor *= self.speedup_scale

        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)