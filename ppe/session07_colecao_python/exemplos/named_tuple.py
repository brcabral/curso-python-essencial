"""
Módulo Collections - Named Tuple
https://docs.python.org/3/library/collections.html#collections.namedtuple

São tuplas, diferenciadas, onde especificamos um nome e também parâmetros

# Recap
tupla = (1, 2, 3)
print(f'tupla: {tupla}')
"""

# Fazendo o import
from collections import namedtuple

# Precisamos definir o nome e os parâmetros

# Forma 1 - Declaração da Named tuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração da Named tuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração da Named tuple (deixa a declaração mais clara)
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando a named tuple
ray = cachorro(idade=2, raca='Chow chow', nome='Ray')
print(f'cachorro ray: {ray}')

# Acessando os dados

# Forma 1
print(f'idade: {ray[0]}')
print(f'raça: {ray[1]}')
print(f'nome: {ray[2]}')

# Forma 2
print(f'idade: {ray.idade}')
print(f'raça: {ray.raca}')
print(f'nome: {ray.nome}')
