"""
Map
 - Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável
 - O retorno da função Map é um Map Object

Com map, fazemos o mapeamento de valores para a função
ex.: map(funcao, valores)
 - A função passada no map(), pode receber apenas 1 parâmetro
"""

import math


def area(raio):
    """Calcula a área de um círculo com raio 'r'"""
    return math.pi * (raio ** 2)


print(f'A área do circulo(r=2) é: {area(2)}')
print(f'A área do circulo(r=5.3) é: {area(5.3)}')
print()

# Calcular o raio da lista abaixo
raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma 1 - Utilizando for
print('>>> Utilizando for <<<')
areas = []
for r in raios:
    areas.append(area(r))
print(f'Areas da lista areas (for): {areas}')

# Forma 2 - Utilizando Map
print('>>> Utilizando map <<<')
areas = map(area, raios)

print(f'Objeto areas: {areas}')
print(f'Tipo da variável nome = {type(areas)}')

print(f'Areas da lista areas (map): {list(areas)}')

# Forma 3 - Utilizando Map e Lambda
print('>>> Utilizando map + lambda <<<')
print(f'Areas da lista areas (map + lambda): {list(map(lambda r: math.pi * (r ** 2), raios))}')

# OBS.: Após utilizar o resultado da função map() ele é excluído da memória e você não poderá usá-lo novamente

print("--------------------------------------------------")
cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27),
           ('Nova York', 28), ('Londres', 22)]
print(f'Lista de cidades e temperaturas(C): {cidades}')

# Converterndo a temperatura para Fahrenheit
c_para_f = lambda dado: (dado[0], (9 / 5) * dado[1] + 32)
print(f'Lista de cidades e temperaturas(F): {list(map(c_para_f, cidades))}')
