# -*- coding: utf-8 -*-

# O diretório 'duas_dimensoes' é um pacotes regular (diretório que obrigatoriamente possui um arquivo __init__.py)

import math
from forma_geometrica import FormaGeometrica


class Circulo(FormaGeometrica):

    def __init__(self, x, y, raio):
        self.x = x
        self.y = y
        self.raio = raio

    def obter_area(self):
        return math.pi * math.pow(self.raio, 2)

    def obter_circuferencia(self):
        return math.pi * 2 * self.raio

