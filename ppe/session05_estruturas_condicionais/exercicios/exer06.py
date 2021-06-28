"""
Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
assim como a diferença existente entre ambos.
"""

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

if numero1 > numero2:
    print("O primeiro número é maior")
    print(f"A diferença entre os números é: {numero1 - numero2}")
elif numero1 < numero2:
    print("O segundo número é maior")
    print(f"A diferença entre os números é: {numero2 - numero1}")
else:
    print("Os números são iguais")
