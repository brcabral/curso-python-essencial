"""
Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros.
A fórmula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume
em metros cúbicos.
"""

cubico = float(input('Digite o volume em metros cúbicos: '))
litros = 1_000 * cubico
print(f'O volume em litros é: {litros}')
