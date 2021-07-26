"""
Random

O que são modulos?
  - São outros arquivos em Python
  - Podemos usar importar e usar funções que estão em outros arquivos Python

Random -> Possuí várias funções para gerar números pseudo-aleatório.
"""
# Há duas formas de utilizar um módulo ou uma função deste.

# Forma 1 - Importando o módulo inteiro (não recomandado)

import random

"""
OBS.: Ao importar o módulo inteiro, todas as funções, atributos, classes e propriedades que estiverem
no módulo ficarão disponíveis (em memória) para serem usadas.
"""

# random() -> Gera um número real pseudo-aleatório entre 0 e 1
# Veja que para utilizar a função random(), colocamos o nome do pacote e o nome da função separados por ponto
print(random.random())

print("--------------------------------------------------")

# Forma 2 - Importando uma função específica (forma recomendada)

# importar apenas a função random do módulo random
from random import random

for i in range(10):
    print(random())

print("--------------------------------------------------")

# uniform() -> Gerar um número real pseudo-aleatório  entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7)) # 7 não é incluído

print("--------------------------------------------------")

# randint() - Gerar números inteiros pseudo-aleatório entre os valores estabelecidos
from random import randint

# Gerar números para apostas da mega-sena
for i in range(6):
    print(randint(1, 61), end=', ')

print()

print("--------------------------------------------------")

# choice() -> Mostrar um valor aleatório em um iterável
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))

print("--------------------------------------------------")

# shuffle() -> Serve para embaralhar os dados
from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10']
print(cartas)

shuffle(cartas)
print(cartas)

shuffle(cartas)
print(cartas)
