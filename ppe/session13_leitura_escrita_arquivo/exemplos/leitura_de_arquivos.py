"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo em Python, utilizamos a função open()

open() -> Na forma mais simples da função, passamos apenas um parâmetro de entrada,
que é o caminho do arquivo a ser lido. Essa função retorna um _io.TextIOWrapper
o qual iremos manipular.

OBS.: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve
existir, caso contrário haverá um erro tipo FileNotFoundError

documentação:
https://docs.python.org/3/library/functions.html#open
"""

arquivo = open('texto.txt')
print(f'Info do arq: {arquivo}')
print(f'Tipo da variável arquivo: {type(arquivo)}')

print("--------------------------------------------------")

# Para ler o conteúdo do arquivo utilizamos a função read()
# A função read() lê todo o conteúdo do arquivo e não apenas uma linha
conteudo_arquivo = arquivo.read()
print(f'Tipo da variável conteudo_arquivo: {type(conteudo_arquivo)}')
print()
print(f'Conteúdo do arquivo: {conteudo_arquivo}')

# OBS: O Python utiliza cursor para trabalhar com arquivos.
# O cursor funciona comoo o cursor de um editor de texto
