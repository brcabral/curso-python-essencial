"""
Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
Gere outro número formado pelos dígitos invertidos do número lido.
 - Exemplo:
   - número lido: 123
   - número gerado = 321
"""

numero = input('Digite um número entre 100 e 999: ')
print(f'O inverso do número digitado é {numero[::-1]}')
