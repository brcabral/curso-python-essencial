"""
Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão
é: G = R * 180 / PI, sendo G o ângulo em graus e R em radianos e PI = 3.14
"""

radiano = float(input('Digite o ângulo em radiano: '))
graus = radiano * 180 / 3.14
print(f'O ângulo em graus é: {graus}')
