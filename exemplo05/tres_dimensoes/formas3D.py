# -*- coding: utf-8 -*-

# O diretório 'tres_dimensoes' é um módulo (diretório que obrigatoriamente possui um arquivo __init__.py vazio)
# Dentro de um módulo é possível existir diversos scripts .py

from duas_dimensoes.retangulo import Retangulo


class Cubo(Retangulo):

    def __init__(self, x, y, base):
        super().__init__(x, y, base, base) # chamando construtor da superclasse
        self.arestaBase = base

    def obter_area(self):
        """
        sobreescrita de método da superclasse Retangulo
        :return:
        """
        return super().obter_area() * 6



class Paralelepipedo(Cubo):

    def __init__(self, x, y, base, altura, arestaBase):
        super().__init__(x, y, arestaBase) # chamando construtor da superclasse
        self.base = base
        self.altura = altura

    def obter_area(self):
        return 2 * (self.base * self.altura + self.base * self.arestaBase + self.altura * self.arestaBase)


