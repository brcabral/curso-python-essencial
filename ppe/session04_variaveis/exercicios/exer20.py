"""
Leia um valor de massa em quilogramas e apresente-o convertido em libras.
A fórmula de conversão é: L = K / 0,45, sendo K a massa em quilogramas
e L a massa em libras
"""

quilograma = float(input('Digite a massa em quilogramas: '))
libra = quilograma / 0.45
print(f'A massa em libras é: {libra}')
