#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from exemplo03.carro import Carro, Motor

if __name__ == '__main__':
    fusca = Carro('fusca', 1960)

    ferrari = Carro('ferrari', 2000)
    ferrari.motor = Motor(8,'etanol')

    print(fusca)
    print(ferrari)
