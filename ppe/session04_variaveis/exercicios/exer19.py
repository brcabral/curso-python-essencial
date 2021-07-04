"""
Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m³.
A fórmula de conversão é: M = L / 1000, sendo L o volume em litros e M o volume
em metros cúbicos.
"""

litros = float(input('Digite o volume em litros: '))
cubico = litros / 1_000
print(f'O volume em metros cúbicos é: {cubico}')
