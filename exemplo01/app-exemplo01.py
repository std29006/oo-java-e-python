#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# Convenção Python PEP8 - https://www.python.org/dev/peps/pep-0008/
# nome_de_funções devem ser em minúsculo e palavras separadas por underscore

# declarando uma função chamada hello_world
def hello_world():
    print("Hello World")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Olá mundo")
    else:
        contador = 0
        for argumento in sys.argv:
            print("argumento[{}]: {}".format(contador, argumento))
            contador = contador + 1

    # invocando uma função do script atual
    hello_world()