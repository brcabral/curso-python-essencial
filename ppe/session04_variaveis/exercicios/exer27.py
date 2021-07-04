"""
Leia um valor de área em hectares e apresente-o convertido em metros quadrados m².
A fórmula de conversão é: M = H * 10000, sendo M a área em metros quadrados
e H a área em hectares
"""

hectare = float(input('Digite a área em hectares: '))
met_quadrado = hectare * 10_000
print(f'A área em metros quadrados é: {met_quadrado}')
