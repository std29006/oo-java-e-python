# -*- coding: utf-8 -*-

class Pessoa(object):
    """"Para representar uma pessoa.
    Em Python não é necessário declarar explicitamente os atributos.
    Todos atributos são públicos por definição, então também não precisamos dos getters and setters, tradicionais do Java
    """

    def __init__(self, nome, dNasc = None):
        """"Construtor da classe.
        O parâmetro dNasc, se não for fornecido durante o instancionamento do objeto, receberá None
        Em Java seria necessário criar 2 construtores. Um com um parâmetro (nome) e outro com dois parâmetros (nome, dNasc)
        """
        self.nome = nome
        self.dataNasc = dNasc

    def definirDataNasc(self, dataNasc):
        self.dataNasc = dataNasc

    def __str__(self):
        """
        Em Java esse método seria equivalente ao toString()
        :return: string concatenando atributos
        """
        resultado = "Nome: " + self.nome
        if self.dataNasc is not None:
            resultado = resultado + ("\nData de nascimento: {}/{}/{}".format(self.dataNasc.day, self.dataNasc.month, self.dataNasc.year))
        return resultado

