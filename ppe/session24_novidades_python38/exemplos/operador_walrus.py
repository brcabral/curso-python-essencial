"""
O operador Walrus permite fazer a atribuição e retorno de valor em uma única expressão

variavel := expressão
"""

nome = 'Geek University'
print(nome)

# Usando Walrus
print(nome := 'Geek University')

print("--------------------------------------------------")

# cesta = []
# fruta = input('Informe a fruta: ')
# while fruta != 'jaca':
#     cesta.append(fruta)
#     fruta = input('Informe a fruta: ')

# Usando Walrus
# cesta = []
# while (fruta := input('Informe a fruta: ')) != 'jaca':
#     cesta.append(fruta)
