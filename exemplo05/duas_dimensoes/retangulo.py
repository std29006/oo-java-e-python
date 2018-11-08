# -*- coding: utf-8 -*-

# O diretório 'duas_dimensoes' é um módulo (diretório que obrigatoriamente possui um arquivo __init__.py vazio)
# Dentro de um módulo é possível existir diversos scripts .py

from forma_geometrica import FormaGeometrica


class Retangulo(FormaGeometrica):
    def __init__(self, x, y, base, altura):
        self.x = x
        self.y = y
        self.base = base
        self.altura = altura

    def obter_area(self):
        return self.altura * self.base
