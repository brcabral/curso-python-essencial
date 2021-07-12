"""
Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.
O volume de um cilindro circular é calcula do por meio da seguinte formula:
V = PI * raio² * altura, onde PI = 3.141592
"""

altura = float(input('Digite a altura do cilindro: '))
raio = float(input('Digite o raio do cilindro: '))
volume = 3.141592 * (raio ** 2) * altura
print(f'O volume do cilindro é: {volume}')
