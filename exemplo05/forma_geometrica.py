# -*- coding: utf-8 -*-

# para classes Abstratas
from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    """
    Essa é uma classe abstrata e com um único método abstrato e um método concreto
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def obter_area(self):
        pass

    def __str__(self):
        """
        Retornar as coordenadas (X,Y)
        :return: (x,y)
        """
        return "({},{})".format(self.x,self.y)