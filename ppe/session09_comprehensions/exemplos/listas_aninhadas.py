"""
Listas aninhadas (Nested Lists)

- Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays:
  - Unidimensionais (Arrays/Vetores);
  - Multidimensionais (Matrizes);

Em Python nós temos as Listas
"""

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Em outras linguagens isso é uma matriz 3 x 3
print(f'Lista listas: {listas}')
print(f'Tipo da variável listas = {type(listas)}')

print("--------------------------------------------------")
# Acessando os elementos de uma lista aninhada
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f'Primeiro elemento da lista: {listas[0]}')
print(f'Segundo elemento do primeiro elemento: {listas[0][1]}')
print(f'Segundo elemento do terceiro elemento: {listas[2][1]}')

print("--------------------------------------------------")
# Iterando com loops em uma lista aninhada
# Usando for
print('>>> Usando for <<<')
for lista in listas:
    for numero in lista:
        print(numero)

# Usando list comprehension
print('>>> Usando list comprehension <<<')
[[print(numero) for numero in lista] for lista in listas]

print("--------------------------------------------------")
# Gerando uma matriz 3 x 3
matriz = [[numero for numero in range(1, 4)] for valor in range(3)]
print(f'Matriz 3 x 3: {matriz}')

print("--------------------------------------------------")
# Gerando um jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(f'Jogo da velha: {velha}')

print("--------------------------------------------------")
velha = [['*' for i in range(1, 4)] for j in range(1, 4)]
for i in velha:
    print(i)
