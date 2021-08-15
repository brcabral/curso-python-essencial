"""
Escrevendo arquivos CSV

A linguagem Python possui duas formas diferentes para escrever dados em arquivos CSV
  - writer
  - DictWriter
"""

# Usando o writer
"""
Para escrever um arquivo CSV com o writer usamos as funções writer e writerow.
 -> Write: Escreve o arquivo
 -> Writerow: Escreve uma linha no arquivo (esse método recebe uma lista)
"""

# from csv import writer
#
# with open('arquivos/filmes1.csv', 'w') as arquivo:
#     escritor_csv = writer(arquivo)
#     filme = None
#     escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
#     while filme != 'sair':
#         filme = input('Informe o nome do filme: ')
#         if filme != 'sair':
#             genero = input('Informe o gênero: ')
#             duracao = input('Informe a duração: ')
#             escritor_csv.writerow([filme, genero, duracao])

print("--------------------------------------------------")

# Usando o DictWriter
"""
Para escrever um arquivo CSV com o DictWriter usamos as funções DictWriter, writeheader e writerow.
 -> DictWriter: Escreve o arquivo
 -> writeheader: Escreve o cabeçalho
 -> Writerow: Escreve uma linha no arquivo (esse método recebe um dicionário)
"""

from csv import DictWriter

with open('arquivos/filmes2.csv', 'w') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração: ')
            escritor_csv.writerow({'Título': filme, 'Gênero': genero, 'Duração': duracao})
