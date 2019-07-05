#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Os diretórios 'duas_dimensoes' e 'tres_dimensoes' são pacotes regulares (diretório que obrigatoriamente possui um arquivo __init__.py vazio)
Dentro de um módulo é possível existir diversos scripts .py

Veja mais em  https://docs.python.org/3/reference/import.html#packages

'''

from duas_dimensoes.circulo import Circulo
from duas_dimensoes.retangulo import Retangulo
from tres_dimensoes.formas3D import Cubo, Paralelepipedo

# Exemplo com classe abstrata e dois níveis de herança

if __name__ == '__main__':
    circulo = Circulo(1, 2, 3.4)
    print("Área do círculo: {}, circunferência: {}".format(round(circulo.obter_area(), 2),
                                                           round(circulo.obter_circuferencia(), 2)))
    quadrado = Retangulo(10, 5, 20, 20)
    print('Área do quadrado: {}'.format(quadrado.obter_area()))

    cubo = Cubo(10, 5, 40)

    paralelo = Paralelepipedo(5, 3, 5, 4, 3)

    print("Área do cubo: {}".format(cubo.obter_area()))
    print("Área do paralelepípedo: {}".format(paralelo.obter_area()))

