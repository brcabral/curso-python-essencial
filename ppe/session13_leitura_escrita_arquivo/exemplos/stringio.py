"""
StringIO

ATENÇÂO!!
  Para ler ou escrever dados em arquivos no sistema operacional é preciso ter permissão
de leitura e escrita em disco

StringIO -> Utilizado para ler e criar arquivos em memória.
"""
# Importar o StringIO
from io import StringIO

mensagem = 'Essa é apenas uma string normal\n'

# Podemos criar o arquivo vazio ou com o conteúdo de uma string.
arquivo = StringIO(mensagem)  # ≃ arquivo = open('arquivo.txt, 'w')

# Agora tendo o arquivo, podemos manipula-lo normalmente
print('Lendo o arquivo...')
print(arquivo.read())

# Adicionar conteúdo
arquivo.write('Outro texto\n')

# É possível movimentar o cursor
arquivo.seek(0)

print('Lendo o arquivo novamente...')
print(arquivo.read())

arquivo.close()
