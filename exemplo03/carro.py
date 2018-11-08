# -*- coding: utf-8 -*-

# Definindo uma classe Carro
class Carro(object):
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
        self.motor = Motor() # instância de uma classe Motor

    def __str__(self):
        return "Modelo: {}, Ano: {}, {}".format(self.modelo, self.ano, self.motor)


# Definindo uma classe Motor
class Motor(object):
    def __init__(self, cilindros = 4, tipoCombustivel = "gasolina"):
        self.cilindros = cilindros
        self.tipoCombustivel = tipoCombustivel

    def __str__(self):
        return "Motor com {} cilindros e movido a {}".format(self.cilindros, self.tipoCombustivel)