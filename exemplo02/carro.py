# -*- coding: utf-8 -*-

'''
Em Python comentários dentro de blocos iniciados/finalizados por 3 apóstrofos são chamados de docstrings e
servem para documentar. Isso seria equivalente aos comentários JavaDOC, que são colocados em blocos /** */

Veja mais sobre classes em: https://docs.python.org/3/tutorial/classes.html


Convenção Python PEP8 - https://www.python.org/dev/peps/pep-0008/

    - NomeDeClasses devem seguir esse formato (chamado de CamelCase)

    - nome_de_métodos_de_classes devem ser em minúsculo e palavras separadas por underscore

    - módulo é um arquivo que contém instruções Python. O nome do arquivo é igual o nome do módulo
      acrescido da extensão .py
      - Este arquivo tem o nome carro.py, então o nome do módulo é: carro. Esse módulo carro é
      importado no arquivo app-exemplo.py

    - modulos devem possuir nome curtos, sempre em minúsculo e underscore pode ser usado se isso 
      tornar mais fácil sua leitura

    
'''


class Carro:

    # atributo da classe e não da instância (equivalente ao static do Java)
    # Em Python não existe o conceito de constante como tem em Java com a palavra 'final'
    VELOCIDADE_MAXIMA = 200

    def __init__(self, modelo = 'Fusca', velocidade = 0):
        '''
        O construtor classe em Python deve ter o nome __init__. Por definição, o primeiro parâmetro de todos métodos
        de uma classe deve receber o nome 'self' e o uso desse seria equivalente a palavra 'this' do Java.

        Python tem o conceito de valores Default para os parâmetros de métodos. Dessa forma, será possível instanciar
        objetos dessa classe fornecendo 2 parâmetros, 1 ou nenhum.

        Em Java seria necessário criar 3 construtores para ter o mesmo comportamento.

        :param modelo: Se não for fornecido um modelo ao instanciar o objeto, então o modelo receberá o valor padrão Fusca
        :param velocidade: Se não for fornecida uma velocidade ao instanciar o objeto, então velocidade receberá 0.
        '''

        # Em Python não é necessário declarar explicitamente os atributos.  Todos atributos são públicos por definição
        #  e assim não precisamos dos getters and setters, tradicionais do Java
        self.modelo = modelo

        # Em Python não existe o conceito de variáveis de instância privadas que só poderão acessadas pelos demais
        # membros da classe. Porém, existe uma convenção que indica se o nome de um membro de classe iniciar
        # com sublinha (underscore), então esse deve ser tratado como um membro privado
        # Veja outro ponto sobre isso em: https://www.python.org/dev/peps/pep-0008/#method-names-and-instance-variables
        self._velocidade = velocidade

    def alterar_velocidade(self, velocidade):
        if velocidade > 0:
            if (self._velocidade + velocidade) <= Carro.VELOCIDADE_MAXIMA:
                self._velocidade += velocidade
            else:
                self._velocidade = Carro.VELOCIDADE_MAXIMA
        else:
            if (self._velocidade + velocidade) >= 0:
                self._velocidade += velocidade
            else:
                self._velocidade = 0


    def __str__(self):
        '''
         Em Java esse método seria equivalente ao toString()
        :return: string concatenando atributos
        '''
        return "Modelo: {}, velocidade: {}".format(self.modelo, self._velocidade)