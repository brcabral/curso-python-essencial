"""
List Comprehension

 - Podemos usar estruturas condigionais lógicas às nossas List Comprehension
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(f'Numeros pares: {pares}')
print(f'Numeros impares: {impares}')

# Refatorando o código acima

# Para qualquer número par o modulo de 2 será 0 e 0 em Python é False
pares = [numero for numero in numeros if not numero % 2]

# Para qualquer número impar o modulo de 2 será 1 e 1 em Python é False
impares = [numero for numero in numeros if numero % 2]

print(f'Numeros pares: {pares}')
print(f'Numeros impares: {impares}')

print("--------------------------------------------------")

result = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(f'Lista de numeros: {result}')
