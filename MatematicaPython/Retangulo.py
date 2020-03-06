#-*- coding: UTF-8 -*-
class Retangulo(object):
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
        self.__area = x * y;
        self.__perimetro = 2 * (x + y);

    def obter_area(self):
        return self.__area;

    def obter_perimetro(self):
        return self.__perimetro;