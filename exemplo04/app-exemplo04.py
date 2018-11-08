#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
from pessoa import Pessoa
from professor import Professor

# Dentro um script .py é possível declarar diversos métodos e também diversas classes
# Para importar todas classes e métodos do script cachorros.py basta:
from cachorros import *

# Porém, a convenção Python PEP8 sugere fazer explicitamente, como está abaixo:
# from cachorros import Cachorro, CaoPolicial

if __name__ == '__main__':
    # Instanciando um objeto da classe Pessoa e passando seu nome no construtor
    pessoa = Pessoa("Juca")
    print("Olá " + pessoa.nome)

    # invocando método str da classe Pessoa
    print(pessoa)

    print("------------")

    # Convenção Python PEP8
    # NomeDeClasses devem seguir esse formato (chamado de CamelCase)
    # nome_de_objetos por outro lado deve ser sempre em minúsculo e com palavras separadas por sublinha
    # modulos_que_possuem classes também devem ser em minúsculo e com palavras separadas por sublinha

    outra_pessoa = Pessoa("Joana", date(2000, 10, 1))
    print(outra_pessoa)

    print("------------")

    # Instanciando um objeto das classes Cachorro e CaoPolicial
    domestico = Cachorro("Totó")
    farejador = CaoPolicial("Brutus")

    # todos atributos são públicos por definição em Python
    print("O nome do cachorro é " + domestico.nome)

    # acessando atributo da classe e não da instância
    print("Cachorro faz parte da família dos {}".format(Cachorro.familia))

    domestico.sentar()

    farejador.farejar()
    farejador.sentar()

    domestico.adicionarTruques('rolar')

    # Todos atributos são públicos em Python
    farejador.truques.append('pular')

    print("{} consegue fazer os seguintes truques: {}" .format(domestico.nome, domestico.truques))
    print("{} consegue fazer os seguintes truques: {}".format(farejador.nome, farejador.truques))

    # É possível criar um novo atributo na instância de uma classe, mesmo que não tenha
    # sido declarado previamente na classe
    pessoa.animal = domestico
    # Porém, o objeto 'outraPessoa' não terá o atributo 'animal'.

    print(pessoa.nome + " tem um cachorro chamado " + pessoa.animal.nome)

    print("------------")


    prof = Professor("Jota", {'123': 'Sinais', '456': 'Programação'})
    print(prof)

    print("------------")
    prof.matricula = "76080-1" # todos atributos são públicos por definição
    print(prof)

    print("------------")

    profa = Professor("Juteide", {'444': 'Algébra', '433': 'Web'}, "12345-6")
    print(profa)

    print(profa.listarDisciplinas())

    print("------------")

    # invocando um método do script cachorro.py que fora importado
    metodoDoScript()