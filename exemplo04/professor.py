# -*- coding: utf-8 -*-

from pessoa import Pessoa

# Professor herda da classe Pessoa
class Professor(Pessoa):

    def __init__(self, nome, disciplinas, matricula = None):
        # invocando construtor da superclasse
        super().__init__(nome)
        # disciplinas é um dicionario (chave, valor). P.ex. {'poo':'Programacao OO'}
        self.disciplinas = disciplinas
        self.matricula = matricula


    def listarDisciplinas(self):
        resultado = "Disciplinas que atua:\n"

        # Percorrendo um dicionário (chave, valor)
        for codigo, nome in self.disciplinas.items():
            resultado = resultado + "Código: {} \t Nome: {}\n".format(codigo, nome)
        return resultado


    def __str__(self):
        resultado = super().__str__()
        if self.matricula is not None:
            resultado = resultado + "\nMatrícula: " + self.matricula
        return  resultado + "\n" +self.listarDisciplinas()
