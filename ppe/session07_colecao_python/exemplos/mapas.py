"""
Mapas -> Conhecido em Python como dicionários

Dicionários em Python são representados por chaves {}
"""
# Iterar sobre dicionários
receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(f'Dicionário receita: {receita}')

print('>>> Imprimindo as chaves do dicionário receita <<<')
for chave in receita:
    print(chave)

print('>>> Imprimindo os valores do dicionário receita <<<')
for chave in receita:
    print(receita[chave])

print('>>> Imprimindo as chaves e os valores do dicionário receita <<<')
for chave in receita:
    print(f'{chave} -> {receita[chave]}')

print('--------------------------------------------------')
# Acessar as chaves dos dicionários
receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(f'Dicionário receita: {receita}')
print(f'Todas as chaves de receita: {receita.keys()}')

print('>>> Imprimindo os valores através do dicionário de chaves <<<')
# Forma recomendada de iterar sobre um dicionário (usando <dict>.keys())
for chave in receita.keys():
    print(receita[chave])

print('--------------------------------------------------')
# Acessar os valores do dicionário
receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(f'Dicionário receita: {receita}')
print(f'Todos os valores de receita: {receita.values()}')

print('>>> Imprimindo os valores através do dicionários de valores <<<')
# Forma recomendada de acessar os valores de um dicionário (usando <dict>.values())
for valor in receita.values():
    print(valor)

print('--------------------------------------------------')
# Desempacotamento de dicionários
receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(f'Dicionário receita: {receita}')

for chave, valor in receita.items():
    print(f'chave={chave} -> valor={valor}')

# Converte o dicionário em um dicionário de itens (lista contendo tuplas)
print(receita.items())

print('--------------------------------------------------')
# Soma*, valor máximo*, valor mínimo*, tamanho
# * Se os valores forem todos inteiros ou reais
receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(f'Soma da receita: {sum(receita.values())}')
print(f'Maior valor da receita: {max(receita.values())}')
print(f'Menor valor da receita: {min(receita.values())}')
print(f'Tamanho da receita: {len(receita)}')
