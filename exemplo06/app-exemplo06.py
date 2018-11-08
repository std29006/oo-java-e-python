#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Exemplo de polimorfismo
'''

# para classes Abstratas
from abc import ABC, abstractmethod


class Arquivo(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def exibir_tipo(self):
        pass

class Pdf(Arquivo):
    def exibir_tipo(self):
        return 'Exibindo conteúdo do PDF'

class Png(Arquivo):
    def exibir_tipo(self):
        return 'Exibindo conteúdo do PNG'


if __name__ == '__main__':

    # Criando uma lista de documentos, na 1a. posição um objeto da classe Pdf e na 2a. posição objeto da classe Png.
    documentos = [Pdf('prova'), Png('ferias')]

    # Percorrendo a lista de documentos
    for arquivo in documentos:
        # Será invocada a implementação do método exibir_tipo() de acordo com o objeto instanciado
        print("{} : {}".format(arquivo.nome, arquivo.exibir_tipo()))