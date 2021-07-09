"""
List Comprehension
 - Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável

# Sintaxe
  - [ dado for dado in iterável ]
"""

numeros = [1, 2, 3, 4, 5]

"""
Para entender melhor o que está devemos dividir a expressão em duas partes
 - Primeira parte: for numero in numeros
 - Segunda parte: numero * 10 
"""
result = [numero * 10 for numero in numeros]
print(f'Múltiplos da lista numeros: {result}')

result = [numero / 2 for numero in numeros]
print(f'Quoeficiente da lista numeros: {result}')


def funcao_quadrado(valor):
    return valor * valor


result = [funcao_quadrado(numero) for numero in numeros]
print(f'Quadrado da lista numeros: {result}')

print("--------------------------------------------------")

# List Comprehension VS Loop
numeros = [1, 2, 3, 4, 5]

# Loop
numeros_dobrados_for = []
for numero in numeros:
    numero = numero * 2
    numeros_dobrados_for.append(numero)

print(f'Lista numeros dobrados usando loop: {numeros_dobrados_for}')

# List comprehension
numeros_dobrados_lc = [numero * 2 for numero in numeros]
print(f'Lista numeros dobrados usando list comprehension: {numeros_dobrados_lc}')

print("--------------------------------------------------")

nome = 'Geek University'
print(f'Upper case na variável nome: {[letra.upper() for letra in nome]}')

print("--------------------------------------------------")

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print(f'Title case na variável amigos: {[letra.title() for letra in amigos]}')

print("--------------------------------------------------")

print(f'Tabuada do 3 =): {[numero * 3 for numero in range(1, 11)]}')

print("--------------------------------------------------")

print(f'Lista booleana: {[bool(valor) for valor in [0, [], "", True, 1, 3.14]]}')

print("--------------------------------------------------")

print(f'Converter numero in string: {[str(numero) for numero in [1, 2, 3, 4, 5]]}')
