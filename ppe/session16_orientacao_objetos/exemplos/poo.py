"""
Programação Orientada a Objeto - POO

  - POO é um paradigma de programação que utiliza o mapeamento de objetos do mundo real
para modelos computacional
  - Paradigma de programação é a forma/metodologia utilizada para pensar/desenvolver sistemas.

Principais elementos da Orientação a objetos
  - Classes -> Modelo do objeto do mundo real
  - Atritubo -> Características do objeto
  - Método -> Comportamento do objeto (função)
  - Construtor -> Método especial utilizado para criar objetos
  - Objeto -> Instância da classe
"""

numero = 10
print()
print(f'Variável numero: {numero}')
print(f'Tipo da variável numero: {type(numero)}')


nome = 'Geek'
print()
print(f'Variável nome: {nome}')
print(f'Tipo da variável nome: {type(nome)}')


class Produto:
    pass


ps4 = Produto()
print()
print(f'Variável ps4: {ps4}')
print(f'Tipo da variável ps4: {type(ps4)}')
