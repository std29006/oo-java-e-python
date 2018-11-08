#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

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

    # invocando um método do script atual
    hello_world()