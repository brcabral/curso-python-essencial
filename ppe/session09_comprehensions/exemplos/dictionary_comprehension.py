"""
Dictionary comprehension

# Sintaxe
  - { chave:valor for valor in iterável }
"""

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(f'Quadrado do dicionário números: {quadrado}')


print("--------------------------------------------------")

numeros = [1, 2, 3, 4, 5]
quadrados = {valor: valor ** 2 for valor in numeros}
print(f'Quadrado do dicionário números: {quadrados}')

# Dicionário não tem elementos repetidos, por isso há menos elementos do que na lista
numeros = [1, 2, 3, 4, 5, 2, 3, 4]
cubo = {valor: valor ** 3 for valor in numeros}
print(f'Cubo do dicionário números: {cubo}')

print("--------------------------------------------------")

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
mix = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(f'Mix de chave/valor: {mix}')

print("--------------------------------------------------")
# Exemplo com lógica condicional

numeros = [1, 2, 3, 4, 5, 6]
result = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(f'Dicionario par/impar: {result}')
