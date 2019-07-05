#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Nesse script é apresentado o básico da sintaxe do Python3

Veja mais informações na documentação oficial: 
https://docs.python.org/3/tutorial/index.html
''' 

def atribuicao_valores():
    i = 10
    print("Valor de i = ", i)

    j = 10 ** 2
    print("{} ao quadrado é: {}".format(i,j))
    print("------------------")

def estruturas_decisao(i):
    '''
    Uma sequência de if ...elif... elif é um substituto para o switch/case que existe no Java e em C/C++
    '''
    if i == 0:
        print("igual a zero")
    elif i > 0:
        print("maior que zero")
    else:
        print("menor que zero")
    print("------------------")

def estruturas_repeticao(i):
    while i > 0:
        print(i)
        i=i-1
    print("------------------")
    for i in range(5):
        print(i)
    print("------------------")
    
def operacoes_com_string():
    '''
    https://docs.python.org/3/tutorial/introduction.html#strings
    '''
    a = "Olá"
    b = a + " Mundo"
    print(b)
    print(b[4]) # M
    print(b[-1]) # o
    print(len(b)) # 9
    print("------------------")

    # objetos
    B = b'em bytes' # objeto byte
    S = 'texto' # objeto str
    
    type(B) # <class 'bytes'>
    type(S) # <class 'str'>

    # convertendo str para bytes
    b = S.encode('utf-8') # ou ainda ascii
    
    # convertendo bytes para str
    s = B.decode()
    print("------------------")


def listas():
    '''
    https://docs.python.org/3/tutorial/introduction.html#lists
    https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
    https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    '''
    primos = [1, 2, 3, 5]
    print(primos[0]) # 1
    primos = primos + [8] # [1, 2, 3, 5, 8]
    primos.append(11) # [1, 2, 3, 5, 7, 11]
    print(len(primos)) # 6
    primos[:] = [] # []

    disciplinas = ['POO', 'STD', 'BCD']

    for disc in disciplinas:
        print(disc)

    # Compreensão de lista 
    quadrados = [x**2 for x in range(5)]

    print(quadrados) # [0, 1, 4, 9, 16]


    print("------------------")

def tuplas():
    '''
    Uma tupla consiste em uma sequência de valores separados por vírgula

    ATENÇÃO: tuplas são imutáveis (em Java seria algo como final). Listas são mutáveis.

    https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

    https://docs.python.org/3/tutorial/datastructures.html#looping-techniques
    '''
    tupla = 123, 456, 'olá'
    print(tupla)
    print(tupla[0])

    # pode-se usar parênteses
    com_par = (789, 'mundo')

    # tupla pode conter tupla
    outra = tupla, ('abc', 'def'), com_par

    print(outra)

    # Para criar uma tupla com 0 elementos
    vazia = ()

    # Para criar uma tupla com 1 elemento é necessário ter uma vírgula no final
    com_um = 'olá mundo', 

    print(len(vazia))
    print(len(com_um))

    # separando elementos de uma tupla
    a, b, c = tupla

    print(a)
    print(b)
    print(c)

    print("------------------")

def conjuntos():
    '''
    Coleção não ordenada de elementos e que não permite elementos duplicados
    https://docs.python.org/3/tutorial/datastructures.html#sets
    '''

    cesta = {'maça', 'pera', 'banana', 'abacate'}

    print(cesta)

    if 'banana' in cesta:
        print("Tem sim")

    if 'uva' not in cesta:
        print("Tem que comprar uva")
    
    print("------------------")

def dicionarios():
    '''
    Elementos de um dicionário são indexados por uma chave.
    Somente tipos imutáveis podem ser usados como chaves.

    https://docs.python.org/3/tutorial/datastructures.html#dictionaries
    https://docs.python.org/3/tutorial/datastructures.html#looping-techniques
    '''
    # criando um dicionário onde o nome é a chave
    matriculas = {'juca' : 123, 'joca' : 456}
    
    # outra forma de criar dicionário
    mats = dict(juca=123, joca=456)
    
    # imprimindo o valor associado a chave 'juca'
    print(matriculas['juca']) # 123

    # alterando o valor associado a chave 'juca'
    matriculas['juca'] = 444

    # obtendo somente uma lista de chaves
    chaves = list(matriculas)
    print(chaves) # ['juca', 'joca']

    # excluindo o elemento 'juca'
    del matriculas['juca'] # {'joca': 456}

    if 'juca' not in matriculas:
        print("Juca não tem matricula")


    # percorrendo os elementos do dicionário
    for chave, valor in matriculas.items():
        print(chave, valor)

    
    print("------------------")


if __name__ == '__main__':

    atribuicao_valores()
    print(estruturas_decisao.__doc__)
    estruturas_decisao(10)
    estruturas_repeticao(10)
    operacoes_com_string()
    listas()
    tuplas()
    conjuntos()
    dicionarios()
