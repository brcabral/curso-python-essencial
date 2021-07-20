"""
Min e Max

max()
 - retorna o maior valor de um iterável ou o maior de dois ou mais elementos
min()
 - retorna o menor valor de um iterável ou o menor de dois ou mais elementos
"""

lista = [1, 8, 4, 99, 34, 129]
print(f'Maior elemento de lista: {max(lista)}')

tupla = (1, 8, 4, 99, 34, 129)
print(f'Maior elemento de tupla: {max(tupla)}')

conjunto = {1, 8, 4, 99, 34, 129}
print(f'Maior elemento de conjunto: {max(conjunto)}')

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 299, 'e': 34, 'f': 129}
print(f'Maior elemento de dicionario: {max(dicionario)}')
print(f'Maior elemento de dicionario.values: {max(dicionario.values())}')

print("--------------------------------------------------")

# Receba dois números e mostre o maior
num1 = 27
num2 = 11
num3 = 30

print(f'O maior número é (num1, num2): {max(num1, num2)}')
print(f'O maior número é (num1, num2, num3): {max(num1, num2, num3)}')

print("--------------------------------------------------")

print(f'Maior valor string: {max("a", "abc", "ab")}')
print(f'Maior valor string: {max("a", "abc", "ab", "b")}')
print(f'Maior valor string: {max("Geek University")}')

print("--------------------------------------------------")
print("--------------------------------------------------")

lista = [1, 8, 4, 99, 34, 129]
print(f'Menor elemento de lista: {min(lista)}')

tupla = (1, 8, 4, 99, 34, 129)
print(f'Menor elemento de tupla: {min(tupla)}')

conjunto = {1, 8, 4, 99, 34, 129}
print(f'Menor elemento de conjunto: {min(conjunto)}')

dicionario = {'a': 11, 'b': 8, 'c': 4, 'd': 299, 'e': 34, 'f': 129}
print(f'Menor elemento de dicionario: {min(dicionario)}')
print(f'Menor elemento de dicionario.values: {min(dicionario.values())}')

print("--------------------------------------------------")

# Receba dois números e mostre o maior
num1 = 27
num2 = 11
num3 = 30

print(f'O menor número é (num1, num2): {min(num1, num2)}')
print(f'O menor número é (num1, num2, num3): {min(num1, num2, num3)}')

print("--------------------------------------------------")

print(f'Menor valor string: {min("a", "abc", "ab")}')
print(f'Menor valor string: {min("abc", "ab", "b")}')
print(f'Menor valor string: {min("Geek University")}')

print("--------------------------------------------------")

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(f'max(nomes): {max(nomes)}')
print(f'min(nomes): {min(nomes)}')

print(f'Nome com mais caracteres: {max(nomes, key=lambda nome: len(nome))}')
print(f'Nome com menos caracteres: {min(nomes, key=lambda nome: len(nome))}')

print("--------------------------------------------------")

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead skin mask', 'tocou': 2},
    {'titulo': 'Back in black', 'tocou': 4},
    {'titulo': 'Too old to rock in roll, too young to die', 'tocou': 32},
]

print(f'Listas de músicas: {musicas}')
print(f'A música que mais tocou: {max(musicas, key=lambda musica: musica["tocou"])}')
print(f'A música que menos tocou: {min(musicas, key=lambda musica: musica["tocou"])}')

print(f'A música que mais tocou: {max(musicas, key=lambda musica: musica["tocou"])["titulo"]}')
print(f'A música que menos tocou: {min(musicas, key=lambda musica: musica["tocou"])["titulo"]}')
