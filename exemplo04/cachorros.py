# -*- coding: utf-8 -*-

# Dentro um script .py é possível declarar diversas funções e também diversas classes


class Cachorro(object):
    """""Para representar um cachorro"""

    familia = 'Canídeos' # atributo da classe e não da instância (equivalente ao static do Java)


    def __init__(self, nome):
        """"Construtor da classe"""
        self.nome = nome
        self.truques = [] # iniciando um atributo da instância, no caso, uma lista vazia

    def sentar(self):
        """"Esse método é para informar que o cachorro sentou"""
        print(self.nome + " foi sentar")

    def adicionarTruques(self, truque):
        self.truques.append(truque)



# Dentro de um mesmo script .py é possível criar mais de uma classe pública. Em Java tal prática não é permitida

class CaoPolicial(Cachorro):
    """"Representa um cão policial farejador que herda da classe Cachorro"""

    def __init__(self, nome):
        """"Construtor da classe e fazendo invocação do construtor da superclasse"""
        super().__init__(nome)

    def farejar(self):
        """"Simular que o cachorro está farejando"""
        print(self.nome + " está farejando")


def funcaoDoScript():
    print("Essa função é do script .py e não pertence a qualquer classe")
    print("é possível usar essa função se o atual script for importado dessa forma: from cachorros import *")