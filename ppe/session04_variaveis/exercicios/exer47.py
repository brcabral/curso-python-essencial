"""
Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha
"""

numero = input('Digite um número entre 1000 e 9999: ')
for i in range(0, len(numero)):
    print(numero[i])
