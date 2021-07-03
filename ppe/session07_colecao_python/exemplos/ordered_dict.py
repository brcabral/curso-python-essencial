"""
Módulo Collections - Ordered Dict
https://docs.python.org/3/library/collections.html#collections.OrderedDict

É um dicionário que nos garante que a ordem de inserção dos elementos será mantida.

# Recap Dicionários
# Em um dicionário comum, a ordem de inserção dos elementos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave: {chave} -> valor: {valor}')
"""

# Fazendo o import
from collections import OrderedDict
dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave: {chave} -> valor: {valor}')

print('--------------------------------------------------')

# Entendendo a diferença entre Dict e Ordered Dict

# Dicionário comum
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(f'dict1 é igual a dict2? {dict1 == dict2}')
# True -> Já que a ordem dos elementos não importa para o dicionário

# Dicionário comum
odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})
print(f'odict1 é igual a odict2? {odict1 == odict2}')
# False -> Já que a ordem dos elementos importa para o OrderedDict
