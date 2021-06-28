"""
Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
 - O número digitado ao quadrado
 - A raiz quadrada do número digitado
"""

numero = float(input("Digite um número: "))

if numero > 0:
    print(f"O número digitado ao quadrado é {numero ** 2}")
    print(f"A raiz quadrada do número digitado é {numero ** 0.5}")
else:
    print("O número é inválido!")
