"""
Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrado do número.
Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""

numero = float(input("Digite um número: "))

if numero > 0:
    print(f"A raiz quadrada do número digitado é {numero ** 0.5}")
else:
    print("O número é inválido!")
