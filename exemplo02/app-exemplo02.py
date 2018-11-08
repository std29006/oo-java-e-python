#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Convenção Python PEP8 - https://www.python.org/dev/peps/pep-0008/

    - NomeDeClasses devem seguir esse formato (chamado de CamelCase)

    - nome_de_objetos por outro lado deve ser sempre em minúsculo e com palavras separadas por sublinha
'''

# equivalente ao import do Java
from carro import Carro


if __name__ == '__main__':
    fusca = Carro()
    print(fusca)

    ferrari = Carro('Ferrari testarossa', 100)
    print(ferrari)

    # O método alterarVelociade garante que um carro não tenha uma velocidade superior a 200 ou menor que 0
    ferrari.alterar_velocidade(400)
    print(ferrari)

    ferrari.alterar_velocidade(-300)
    print(ferrari)

    fusca.modelo = 'Fusca 1970'
    print(fusca)

    # isso cria uma nova variável no objeto 'fusca', mas não tem relação com os atributos definidos na classe Carro
    fusca.velocidade = 400
    print(fusca)

    # Apesar do atributo iniciar com o underscore (que remete a ideia de membro privado), ainda assim será possível acessá-lo diretamente
    fusca._velocidade = 400
    print(fusca)

    fusca._velocidade = -100
    print(fusca)

