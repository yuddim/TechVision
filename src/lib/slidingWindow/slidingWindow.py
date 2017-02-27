# coding: utf8


from cv2 import *


class SlidingWindow:
    '''
    Объект для работы с плавающим окном. (пока cpu)
    '''

    def __init__(self, width=150, height=150, step_x=50, step_y=10, delta=250):
        '''
        Конструктор объета
        :param width: Ширина скользящего окна.
        :param height: Высота скользящего окна.
        :param step_x: Шаг скользящего окна по x.
        :param step_y: Шаг скользящего окна по y.
        :return: Экземпляр объекта.
        '''
        self.width = width;
        self.height = height;
        self.step_x = step_x;
        self.step_y = step_y;
        self.delta = delta;

    def detect_callback(self, detect):
        '''
        Set function detector
        :param detect: detection function
        :return: void.
        '''
        self.detect = detect

    def _solve_first_position(self, _w, w_img):
        '''
        Вычисление положения первого окна.
        :param _w:  параметр объекта.
        :param w_img: параметр изображения.
        :return: одна координата смещения.
        '''
        w = w_img % _w
        if (w == 0):
            return _w
        else:
            return w / 2

    def sliding_windows(self, img):
        '''
        Вычисдение скользящего окна.
        :param img: Изображение для вычисления
        :return: Массив изображений
        '''
        if (not img is None):
            h_img = img.shape[0]
            w_img = img.shape[1]
            is_width = True
            is_heigh = True
            while is_width | is_heigh:
                # определили смещение
                _y_delta = self._solve_first_position(self.height, h_img)
                _x_delta = self._solve_first_position(self.width, w_img)
                y = _y_delta

                while (y + self.height) <= (h_img - _y_delta):
                    x = _x_delta
                    # x,y - текущие координаты

                    while (x + self.width) <= (w_img - _x_delta):
                        _img = img.copy()
                        # TODO: Тут будет вызов функции распознавания
                        rectangle(_img, (x, y), (x + self.width, y + self.height), (255, 7, 7), 2)
                        imshow('test0', _img)
                        waitKey(5)
                        x = x + self.step_x
                    y = y + self.step_y

                self.width = self.width + self.delta
                self.height = self.height + self.delta
                is_width = self.width <= w_img
                is_heigh = self.height <= h_img

        else:
            return 0
