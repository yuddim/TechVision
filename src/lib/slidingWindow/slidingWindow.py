# coding: utf8

import cv2


class SlidingWindow:
    '''
    Объект для работы с плавающим окном.
    '''

    def __init__(self, width=10, height=10, step=1):
        '''
        Конструктор объета

        :param width: Ширина скользящего окна.
        :param height: Высота скользящего окна.
        :param step: Шаг скользящего окна.
        :return: Экземпляр объекта.
        '''
        self.width = width;
        self.height = height;
        self.step = step;

    def sliding_windows(self, img):
        '''
        Вычисдение скользящего окна.

        :param img: Изображение для вычисления
        :return: Массив изображений
        '''
        if(img):
            print 1
        else:
            return None

