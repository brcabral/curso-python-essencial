"""
Range

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.
"""

"""
range(valor_de_parada)
 - início padrão 0, valor_de_parada não inclusive e passo de 1 em 1
"""
for num in range(11):
    print(num)

print("--------------------------------------------------")

"""
range(valor_de_inicio, valor_de_parada)
 - valor_de_inicio especificado pelo usuário, valor_de_parada não inclusive e passo de 1 em 1
"""
for num in range(2, 11):
    print(num)

print("--------------------------------------------------")

"""
range(valor_de_inicio, valor_de_parada, passo)
 - valor_de_inicio especificado pelo usuário, valor_de_parada não inclusive e passo especificado pelo usuário
"""

for num in range(1, 10, 2):
    print(num)

print("--------------------------------------------------")

"""
range(valor_de_inicio, valor_de_parada, passo)
 - valor_de_inicio especificado pelo usuário, valor_de_parada não inclusive e passo especificado pelo usuário
"""

for num in range(10, 1, -2):
    print(num)

print("--------------------------------------------------")

lista = list(range(10))
print(lista)
