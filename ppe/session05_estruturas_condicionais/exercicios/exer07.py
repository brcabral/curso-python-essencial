"""
Faça um programa que receba dois números e mostre o maior.
Se por acaso, os dois númros forem iguais, imprima a mensagem "Números iguais"
"""

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O primeiro número é maior")
elif numero1 < numero2:
    print("O segundo número é maior")
else:
    print("Números iguais")
