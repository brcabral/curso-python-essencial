"""
Leia um valor de de comprimento em jardas e apresente-o convertido em metros.
A fórmula de conversão é: M = 0,91 * J, sendo J o comprimento em jardas
e M o comprimento em metros
"""

jarda = float(input('Digite a comprimento em jardas: '))
metro = jarda * 0.91
print(f'O comprimento em metros é: {metro}')
