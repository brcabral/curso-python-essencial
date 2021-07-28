"""
Bloco with

Passos para trabalhar com arquivos
  1 - Abrir o arquivo
  2 - Manipular o arquivo
  3 - Fechar o arquivo

with -> O with é utilizado para criar um contexto de trabalho, onde os recursos utilizados
serão fechados no fim do bloco.
"""

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(f'O arquivo está fechado? {arquivo.closed}')

print(f'O arquivo está fechado? {arquivo.closed}')
