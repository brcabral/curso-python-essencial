"""
Leia um valor de área em acres e apresente-o convertido em metros quadrados m².
A fórmula de conversão é: M = A * 4048,58, sendo M a área em metros quadrados
e A a área em acres
"""

acre = float(input('Digite a área em acres: '))
met_quadrado = acre * 4048.58
print(f'A área em metros quadrados é: {met_quadrado}')
