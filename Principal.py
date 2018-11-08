#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# seres é um módulo (diretório que obrigatoriamente possui um arquivo __init__.py vazio)
# Dentro de um módulo é possível existir diversos scripts .py
# Dentro um script .py é possível declarar diversos métodos e também diversas classes

from pessoa import Pessoa
from professor import Professor


# Importando todas classes e métodos do script cachorros.py
#from seres.cachorros import *
# Porém, a convenção Python PEP8 sugere para fazer explicitamente
from cachorros import Cachorro, CaoPolicial
from tres_dimensoes import Cubo, Paralelepipedo

from duas_dimensoes.circulo import Circulo
from duas_dimensoes import Retangulo





def primeiro_exemplo():
    # Instanciando um objeto da classe Pessoa e passando seu nome no construtor
    p = Pessoa("Juca")
    print("Olá " + p.nome)

    # Instanciando um objeto das classes Cachorro e CaoPolicial
    domestico = Cachorro("Totó")
    farejador = CaoPolicial("Brutus")

    print("Meu animal de estimação chama-se " + domestico.nome)

    print("Cachorro faz parte da família dos {}".format(Cachorro.familia))

    domestico.sentar()

    farejador.farejar()
    farejador.sentar()

    domestico.adicionarTruques('rolar')

    # Todos atributos da classe são públicos em Python
    farejador.truques.append('pular')

    print(domestico.truques)
    print(farejador.truques)


    p.definirAnimalEstimacao(domestico)

    print(p.nome + " tem um cachorro chamado " + p.animal.nome)





def segundo_exemplo():
    # Instanciando um professor
    prof = Professor("Jota", {'123': 'Sinais', '456': 'Programação'})

    prof.listarDisciplinas()


def terceiro_exemplo():
    circulo = Circulo(1,2, 3.4)
    print("Área do círculo: {}, \t circunferência: {}".format(round(circulo.obter_area(), 2), round(circulo.obter_circuferencia(), 2)))

    quadrado = Retangulo(10,5, 20, 20)
    print('Área do quadrado: {}'.format(quadrado.obter_area()))


    cubo = Cubo(10, 5, 40)

    paralelo = Paralelepipedo(5, 3, 5, 4, 3)

    print("Área do cubo: {}".format(cubo.obter_area()))
    print("Área do paralelepípedo: {}".format(paralelo.obter_area()))


# O uso dessa opção é interessante, caso queira garantir que as instruções
# só serão executadas se o script for interpretado e não quando for importado por outro script
if __name__ == '__main__':
    primeiro_exemplo()

    segundo_exemplo()

    terceiro_exemplo()