"""
Any e All

any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna false.
all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.
"""
# Exemplo all()
from builtins import print

lista1 = [0, 1, 2, 3, 4]
lista2 = [1, 2, 3, 4]
lista3 = []

print(f'Lista 1: {all(lista1)}')  # Todos os elementos são verdadeiros? False
print(f'Lista 2: {all(lista2)}')  # Todos os elementos são verdadeiros? True
print(f'Lista 3: {all(lista3)}')  # Todos os elementos são verdadeiros? True

print()

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(f'Todos nomes começam com C? {all([nome[0] == "C" for nome in nomes])}')

print()

print(f'Contem letras? {all([False for letra in "aio" if letra not in "aeiou"])}')
print(f'Contem letras? {all([False for letra in "keio" if letra not in "aeiou"])}')

print()

print(f'Todos são par? {all([False for numero in [4, 2, 10, 6, 8] if numero % 2])}')
print(f'Todos são par? {all([False for numero in [4, 2, 10, 6, 8, 9] if numero % 2])}')

print()

print(f'Todos são par? {all([numero % 2 == 0 for numero in [4, 2, 10, 6, 8]])}')
print(f'Todos são par? {all([numero % 2 == 0 for numero in [4, 2, 10, 6, 8, 9]])}')

print("--------------------------------------------------")

# Exemplo any()
lista4 = [0, 1, 2, 3, 4]
lista5 = [1, 2, 3, 4]
lista6 = []
lista7 = [0, 0, 0]
lista8 = [0, 0, 1, 0]
lista9 = [0, False, {}, [], ()]

print(f'Lista 4: {any(lista4)}')  # Algum elemento é verdadeiros? True
print(f'Lista 5: {any(lista5)}')  # Algum elemento é verdadeiros? True
print(f'Lista 6: {any(lista6)}')  # Algum elemento é verdadeiros? False
print(f'Lista 7: {any(lista7)}')  # Algum elemento é verdadeiros? False
print(f'Lista 8: {any(lista8)}')  # Algum elemento é verdadeiros? True
print(f'Lista 9: {any(lista9)}')  # Algum elemento é verdadeiros? False

print()

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(f'Algum nome começam com C? {any([nome[0] == "C" for nome in nomes])}')
print(f'Algum nome começam com L? {any([nome[0] == "L" for nome in nomes])}')
print(f'Algum nome começam com V? {any([nome[0] == "V" for nome in nomes])}')
