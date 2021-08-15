"""
Lendo arquivos CSV
 -> CSV: Comma Separeted Values (Valores Separados por Vírgulas)
   -> Porém pode ser usado com qualquer outro tipo de separador: virgula, ponto virgula, pipe, etc

Site para obter arquivos com dados para teste
 -> https://dados.gov.br/dataset

"""

# Forma 1 - Não ideal
with open('arquivos/lutadores.csv') as arquivo:
    dados = arquivo.read()
    # print(f'Tipo da variável nome: {type(dados)}')
    dados = dados.split(',')[2:]
    print(dados)

print("--------------------------------------------------")

"""
A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV
  - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
  - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDict;
"""

# Usando o Reader
from csv import reader

with open('arquivos/lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # Pular o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} centímetros')

print("--------------------------------------------------")

# Usando o DictReader
from csv import DictReader

with open('arquivos/lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f'{linha["Nome"]} nasceu no(a) {linha["País"]} e mede {linha["Altura (em cm)"]} centímetros')

print("--------------------------------------------------")

# Definindo outro separador
from csv import reader, DictReader

with open('arquivos/lutadores_ponto_virtula.csv') as arquivo:
    leitor_reader = reader(arquivo, delimiter=';')
    for linha in leitor_reader:
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} centímetros')
    print('')
    arquivo.seek(0)
    leitor_dict_reader = DictReader(arquivo, delimiter=';')
    for linha in leitor_dict_reader:
        print(f'{linha["Nome"]} nasceu no(a) {linha["País"]} e mede {linha["Altura (em cm)"]} centímetros')
