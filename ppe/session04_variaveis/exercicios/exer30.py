"""
Leia um valor em real (R$) e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares.
"""

real = float(input('Digite o valor em real (R$): '))
dolar = float(input('Digite a cotação do dolar: '))

print(f'O total é : US${real / dolar}')
