"""
Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = raiz(a² + b²). Faça um programa que receba os valores de a e b e calcule
o valor da hipotenusa através da equação. Imprima o resultado dessa operação
"""

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
hipotenusa = ((a ** 2) + (b ** 2)) ** 0.5
print(f'O valor da hipotenusa é: {hipotenusa}')
