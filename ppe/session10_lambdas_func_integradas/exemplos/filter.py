"""
Filter
 - Serve para filtrar dados de uma determinada coleção.
"""
# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dado utilizando a função mean()
media = statistics.mean(dados)
print(f'A média é de {media}')

# OBS.: Assim como a função map(), o filter() recebe dois parâmetros
# sendo uma função e um iterável
result = filter(lambda valor: valor > media, dados)
print(f'Os valores acima da média são: {list(result)}')

# OBS.: Após utilizar o resultado da função filter() ele é excluído da memória e você não poderá usá-lo novamente
print(f'Reimprimindo os valores acima da média: {list(result)}')

print("--------------------------------------------------")

# Removendo dados faltantes
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Uruguai']
print(f'Lista de países: {paises}')

# Forma 1 - Usando None
filter_none = filter(None, paises)
print(f'Lista filtrada dos países (none): {list(filter_none)}')

# Forma 2 - Usando Lambda
filter_lambda = filter(lambda pais: len(pais) > 0, paises)
# filter_lambda = filter(lambda pais: pais != '', paises)
print(f'Lista filtrada dos países (lambda): {list(filter_lambda)}')

print("--------------------------------------------------")

usuarios = [
    {'usuario': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizza']},
    {'usuario': 'carla', 'tweets': ['Eu amo meu gato']},
    {'usuario': 'jeff', 'tweets': []},
    {'usuario': 'bob123', 'tweets': []},
    {'usuario': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'usuario': 'gal', 'tweets': ['Ouvindo músicas da minha chará Gal Costa']}
]
print(f'Listas dos usuários: {usuarios}')

# Filtrar os usuários inativos (não tem nenhum tweet)
# Forma 1 - Contanto a quantidade de tweets
inativos_count = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(f'Listas dos usuários inativos (count): {inativos_count}')

# Forma 2 - Verificando a lista
inativos_lista = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(f'Listas dos usuários inativos (vendo lista): {inativos_lista}')

print("--------------------------------------------------")

# Combinando filter() e map()
nomes = ['Vanessa', 'Ana', 'Maria', 'Carla', 'Lucy', 'Camila', 'Yane']

# Criar uma lista contendo 'Sua instrutora é {nome}', desde que o nome tenha menos de 5 caracteres
# Forma 1 - Por partes
filtro = filter(lambda nome: len(nome) < 5, nomes)
lista_parte = list(map(lambda nome: f'Sua instrutora é {nome}', filtro))
print(lista_parte)

# Forma 2 - Direto
lista_parte = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista_parte)
