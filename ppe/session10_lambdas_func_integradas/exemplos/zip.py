"""
Zip
  zip() -> Cria um iterável (zip object) que agrega elemento de cada um dos iteráveis passado como entrada em pares.
"""

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2, 'abc')

print(f'Variável nome: {zip1}')
print(f'Tipo da variável nome: {type(zip1)}')

# Através do zip object, podemos gerar uma lista, tupla, set ou dicionário
print(f'Lista zip1: {list(zip1)}')

# OBS.: Após utilizar o resultado da função zip() ele é excluído da memória e você não poderá usá-lo novamente
zip1 = zip(lista1, lista2, 'abc')
print(f'Tupla zip1: {tuple(zip1)}')

zip1 = zip(lista1, lista2, 'abc')
print(f'Set zip1: {set(zip1)}')

zip1 = zip('abc', lista2)
print(f'Dicionário zip1: {dict(zip1)}')

# OBS.: O zip() cria N tuplas com os iteráveis passados, onde N será a quantidade de elementos dos iteráveis.
# Caso esteja trabalhando com iteráveis de tamanhos diferentes, a quantidade de tuplas retornada será do
# iterável de menor tamanho
lista3 = [7, 8, 9, 10, 11]
zip2 = zip(lista1, lista2, lista3)
print(f'Lista zip2: {list(zip2)}')

print("--------------------------------------------------")

# Podemos utilizar diferentes iteráveis com zip
tupla = (1, 2, 3, 4, 5)
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(f'Resultado de zt: {list(zt)}')

# Lista de tuplas
dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
zip_dados = zip(*dados)
print(f'Resultado de zip_dados: {list(zip_dados)}')

print("--------------------------------------------------")

# Dado a lista de alunos e as notas da primeira e segunda prova
# crie um dicionário com o nome e a maior nota

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

# Forma 1 - Usando Dictionary Comprehension
final_dict = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(f'Dicionário com aluno e maior nota (dic compre): {final_dict}')

# Forma 2 - Usando o map
final_map = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(f'Dicionário com aluno e maior nota (map): {dict(final_map)}')
