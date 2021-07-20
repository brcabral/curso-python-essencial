"""
Sorted
 Como o próprio nome diz, sorted() serve para ordenar elementos.

OBS.: Não confunda sorted() com a função sort(). O sort() só funciona em listas.
O sort() pode ser usado apenas em listas, já o sorted() podemos usar em qualquer iterável
"""

numeros = [6, 1, 8, 2]
print(f'Lista numeros: {numeros}')
print(f'Lista numeros com sorted: {sorted(numeros)}')
print(f'Lista numeros: {numeros}')

# OBS.: O sort() ordena a própria lista, já o sorted() gera uma nova

print("--------------------------------------------------")

numeros = (7, 4, 2, 6)
print(f'Tupla numeros: {numeros}')
print(f'Tupla numeros com sorted: {sorted(numeros)}')
print(f'Tupla numeros: {numeros}')

# OBS.: O método sorted() sempre retorna uma lista

print("--------------------------------------------------")
# Adicionando parâmetros ao sorted()
numeros = [6, 1, 8, 4, 2, 5, 3, 7]
print(f'Lista numeros: {numeros}')

# Reverse
print(f'Lista numeros ordenada reversa: {sorted(numeros, reverse=True)}')

print("--------------------------------------------------")

usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizza']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato'], 'cor': 'preto', 'musica': 'rock'},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': [], 'cor': 'amarelo'},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': ['Ouvindo músicas da minha chará Gal Costa']}
]
print(f'Listas dos usuários: {usuarios}')
print(f'Listas dos usuários por tamanho: {sorted(usuarios, key=len)}')
print(f'Ordenando pelo username: {sorted(usuarios, key=lambda usuario: usuario["username"])}')
print(f'Ordenando pela quantidade de tweet: {sorted(usuarios, key=lambda usuario: len(usuario["tweets"]))}')

print("--------------------------------------------------")

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead skin mask', 'tocou': 2},
    {'titulo': 'Back in black', 'tocou': 4},
    {'titulo': 'Too old to rock in roll, too young to die', 'tocou': 32},
]

print(f'Listas de músicas: {musicas}')
print(f'Ordena as músicas (menos tocada -> mais tocada): {sorted(musicas, key=lambda musica: musica["tocou"])}')
print(f'Ordena as músicas (mais tocada -> menos tocada): '
      f'{sorted(musicas, key=lambda musica: musica["tocou"], reverse=True)}')

print("--------------------------------------------------")

nome = 'Geek University'
print(f'Variável nome: {nome}')
print(f'Variável nome ordenada: {sorted(nome)}')
