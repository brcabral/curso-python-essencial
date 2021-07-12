"""
Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lido
"""

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

resultado = (num1 ** 2) + (num2 ** 2) + (num3 ** 2)
print(f'A soma dos quadrados dos números digitados é: {resultado}')
