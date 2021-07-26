"""
Trabalhando com módulos Built-in (módulos integrados - já vem instalados no Python)

Documentação dos módulos
https://docs.python.org/3.8/py-modindex.html
"""

# Utilizando alias (apelidos) para módulos/funções
import random as rdm
print(rdm.random())

from random import randint as rdi
print(rdi(5, 89))

print("--------------------------------------------------")

# Podemos importar todas as funções de um módulo utilizando o *
from random import *
print(random())

print("--------------------------------------------------")

# Importar e atribuir um alias a mais de uma função
from random import random as rdm, randint as rdi
print(rdm())
print(rdi(1, 10))

print("--------------------------------------------------")

# Podemos utilizamos uma tupla para colocar múltiplos imports de um mesmo modulo
from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())
print(randint(3, 7))

lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

print(choice('University'))
