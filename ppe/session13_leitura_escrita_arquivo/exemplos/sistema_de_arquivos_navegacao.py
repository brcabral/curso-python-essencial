"""
Sistema de arquivos e navegação
  Para fazer manipulação de arqivos do sistema operacional, é preciso importar o modulo os
"""

# Fazer o import do os
import os

# Fazer o import do sys
import sys

# getcwd() -> get current work directory (obter o diretório de trabalho corrente)
# Retorna o caminho absoluto
print(f'Current directory: {os.getcwd()}')

# chdir() -> mudar o diretório
os.chdir('..')
print(f'Current directory: {os.getcwd()}')

print("--------------------------------------------------")

# Verificar se um diretório é absoluto ou relativo
print(f'/home/breno/Documents: {os.path.isabs("/home/breno/Documents")}')
print(f'session13_leitura_escrita_arquivo/exemplos: {os.path.isabs("session13_leitura_escrita_arquivo/exemplos")}')

print("--------------------------------------------------")

# Verificar sistema de arquivo (posix or nt)
# posix (Linux e Mac) | nt (Windows)
print(f'System file: {os.name}')

print("--------------------------------------------------")

# Verificar o sistema operacional
print(f'OS: {sys.platform}')

print("--------------------------------------------------")

# Obter mais detalhes do sistema operacional
print(f'OS details: {os.uname()}')

print("--------------------------------------------------")

# Concatenar diretórios
print(f'Current directory: {os.getcwd()}')
new_dir = os.path.join(os.getcwd(), 'exemplos', 'arquivos')
os.chdir(new_dir)
print(f'Current directory: {os.getcwd()}')

print("--------------------------------------------------")

# listdir() -> Listar os arquivos e diretórios
print(f'List of files: {os.listdir()}')

# Contar quantidades de arquivos em um diretório
print(f'Number of files: {len(os.listdir())}')

print("--------------------------------------------------")

# scandir() -> Listar os arquivos e diretórios

scanner = os.scandir()
arquivos = list(scanner)

print(f'Detalhes dos arquivos: {arquivos}')

"""
Inodes são estruturas responsáveis por conter informações básicas sobre arquivos e pastas,
como permissões de acesso, identificação dos donos dos arquivos, data e hora do último
acesso e alterações, tamanho
"""
print(f'É um diretório? {arquivos[0].is_dir()}')
print(f'É um arquivo? {arquivos[0].is_file()}')
print(f'É um link simbólico? {arquivos[0].is_symlink()}')
print(f'inode do arquivo: {arquivos[0].inode()}')
print(f'Nome do arquivo: {arquivos[0].name}')
print(f'Caminho do arquivo: {arquivos[0].path}')
print(f'Estatísticas do arquivo: {arquivos[0].stat()}')

# OBS.: Após usar a função scandir() é preciso fechá-la
scanner.close()
