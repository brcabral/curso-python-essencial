"""
Módulo Collections - Default Dict
https://docs.python.org/3/library/collections.html#collections.defaultdict

Ao criar um dicionário com default dict, nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre
que não houver um valor difinido. Caso tentemos acessar uma chave que não existe,
essa chave será criada e o valor default será atribuído.

OBS.: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada
e retornar valores.

# Recap Dicionários
dicionario = {'curso': 'Programação em Python: Essencial'}
print(f'dicionário: {dicionario}')
print(f'dicionário chave curso: {dicionario["curso"]}')
# print(f'dicionário chave outro: {dicionario["outro"]}')  # KeyError
"""

# Fazendo o import
from collections import defaultdict

# Nesse exemplo a função lambda criada
# não recebe nenhum parâmetro e retorno valor 0
dicionario = defaultdict(lambda: '0')

dicionario['curso'] = 'Programação em Python: Essencial'
print(f'dicionário: {dicionario}')

# Caso fosse um dicionário comum, daria KeyError por não existir a chave outro
print(f'dicionário chave outro: {dicionario["outro"]}')
print(f'dicionário após acessar chave outro: {dicionario}')
