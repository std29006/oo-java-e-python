#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

Exemplo sobre tratamento de exceções.

Execute o script e:

- No primeiro teste forneça 2 números inteiros. 

- No segundo teste forneça uma letra para um ou para os dois operandos

'''


def sem_tratar(a, b):
    resultado = int(a) + int(b)

    print("Resultado da soma é: {}".format(resultado))


def com_tratamento(a, b):
    try:

        resultado = int(a) + int(b)
        print("Resultado da soma é: {}".format(resultado))

    except ValueError as e:
        print("Não foi possível fazer a soma. Veja o erro: {}".format(e))




if __name__ == '__main__':
    a = input("Entre com o primeiro operando: ")
    b = input("Entre com o segundo operando: ")

    com_tratamento(a, b)
    sem_tratar(a, b)