"""
Set comprehension
"""

numeros = {num for num in range(1, 7)}
print(f'Conjunto de números: {numeros}')

print("--------------------------------------------------")

quadrados = {x ** 2 for x in range(10)}
print(f'Conjunto de números ao quadrado: {quadrados}')

print("--------------------------------------------------")

# DESAFIO! Faça uma alteração na estrutura acima para gerar um dicionário ao invés de um set
dic_quadrado = {x: x ** 2 for x in range(10)}
print(f'Dicionario de números ao quadrado: {dic_quadrado}')

print("--------------------------------------------------")

letras = {letra for letra in 'Geek University'}
print(f'Letras: {letras}')
