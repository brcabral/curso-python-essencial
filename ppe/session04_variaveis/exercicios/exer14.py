"""
Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão
é: R = G * PI / 180, sendo G o ângulo em graus e R em radianos e PI = 3.14
"""

graus = float(input('Digite o ângulo em graus: '))
radiano = graus * 3.14 / 180
print(f'O ângulo em radiono é: {radiano}')
