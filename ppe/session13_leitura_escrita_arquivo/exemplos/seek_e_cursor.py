"""
Seek e Cursor

seek() -> É utilizado para movimentar o cursor pelo arquivo
"""

arquivo = open('texto.txt')
print(f'Conteúdo do arquivo: {arquivo.read()}')
print(f'Conteúdo do arquivo: {arquivo.read()}')

# seek() -> A função seek() é utilizada para movimentar o cursor pelo arquivo.
# Ela recebe um parâmetro que indica a nova posição do cursor.

# Movimenta o cursor para a posição 0 (zero - início) do arquivo
arquivo.seek(0)
print(f'Conteúdo do arquivo: {arquivo.read()}')

arquivo.seek(22)
print(f'Conteúdo do arquivo: {arquivo.read()}')

print("--------------------------------------------------")

arquivo = open('texto.txt')

# readline() -> Ler o conteúdo do arquivo linha a linha
print(f'Conteúdo da 1ª linha: {arquivo.readline()}')
print(f'Conteúdo da 2ª linha: {arquivo.readline()}')
print(f'Conteúdo da 3ª linha: {arquivo.readline()}')
print(f'Conteúdo da 4ª linha: {arquivo.readline()}')

print("--------------------------------------------------")

arquivo = open('texto.txt')

# readlines() -> Ler o conteúdo do arquivo e retorna uma lista, onde cada linha é um elemento da lista
print(f'Lista com o conteúdo do arquivo: {arquivo.readlines()}')

print("--------------------------------------------------")

"""
OBS.: Quando abrimos um arquivo é criada uma conexão entre o arquivo no disco e o programa.
Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo devemos fechar
essa conexão, para isso utilizamos a função close()
"""

# Abrir o arquivo
arquivo = open('texto.txt')

# Trabalhar com o arquivo
print(f'Conteúdo do arquivo: {arquivo.read()}')

# arquivo.closed -> Verifica se o arquivo está aberto ou fechado
print(f'O arquivo está fechado? {arquivo.closed}')

# Fechar o arquivo
arquivo.close()

print(f'O arquivo está fechado? {arquivo.closed}')

# OBS.: Se tentarmos manipular um arquivo fechado, teremos um ValueError

print("--------------------------------------------------")

arquivo = open('texto.txt')

# Limitar a quantidade de caracteres lido
print(f'Limitando a leitura do arquivo a 56 caracteres: {arquivo.read(56)}')
print(f'Continuar lendo (10) o arquivo do 57 caractere: {arquivo.read(10)}')
