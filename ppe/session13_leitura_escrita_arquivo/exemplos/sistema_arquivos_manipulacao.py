"""
Sistema de arquivos manipulação
"""
import os

# Verificar se um arquivo ou diretório existe

# Arquivos
print(f'Arquivo arquivos/arquivos.txt existe? {os.path.exists("arquivos/arquivo.txt")}')
print(f'Arquivo arquivos/frutas.txt existe? {os.path.exists("arquivos/frutas.txt")}')

# Diretórios
# Path relativo
print(f'Diretório geek existe? {os.path.exists("geek/")}')
print(f'Diretório arquivos existe? {os.path.exists("arquivos")}')

# Path absoluto
print(f'Diretório /home/breno/Pictures existe? {os.path.exists("/home/breno/Pictures")}')

print("--------------------------------------------------")

# Criar arquivos
# Forma 1
open('arquivos/arquivo-teste1.txt', 'w').close()

# Forma 2
open('arquivos/arquivo-teste2.txt', 'a').close()

# Forma 3
with open('arquivos/arquivo-teste3.txt', 'w') as arquivo:
    pass  # pass = não fazer nada

# Forma 4
# OBS1.: O mknod pode não funcionar no MacOs, pois requer poderes administrativos para executar o comando
# OBS2.: Ao tentar criar um arquivo com mknod(), se o mesmo já existir, será lançado o erro FileExistsError
try:
    os.mknod('arquivos/arquivo-teste4.txt')
except FileExistsError:
    print('Arquivo já existe')

print("--------------------------------------------------")

# Criar diretórios
# OBS.: Ao tentar criar um diretório com mkdir(), se o mesmo já existir, será lançado o erro FileExistsError
try:
    os.mkdir('templates')
except FileExistsError:
    print('Diretório já existe')

# OBS.: Ao passar mais de um diretório, o Python vai entender que os primeiros já existem
# e tentará criar apenas o último
try:
    os.mkdir('templates/geek/university')
except FileExistsError:
    print('Diretório já existe')
except FileNotFoundError:
    print('Diretório não existe')

# Criar toda a árvore de diretório passada
try:
    os.makedirs('templates/geek/university')
except FileExistsError:
    print('Os diretórios já existem')

# Cria toda a árvore de diretório passada. Caso algum diretório já exista, não será lançado erro
os.makedirs('templates2/geek2/university2', exist_ok=True)

print("--------------------------------------------------")

try:
    os.mknod('templates2/geek2/university2/arquivo-teste1.txt')
except FileExistsError:
    print('Arquivo já existe')

# Renomear arquivos e diretórios

# Diretório
try:
    os.rename('templates2', 'new_dir')
except OSError:
    print('O diretório não está vazio')
# OBS.: Se o diretório não existir será lançado um FileNotFoundError

try:
    os.rename('new_dir/geek2/university2', 'python')
except OSError:
    print('O diretório não está vazio')
# OBS.: Se o diretório não estiver vazio será lançado um OSError

# Arquivo
try:
    os.rename('new_dir/geek2/university2/arquivo-teste1.txt', 'new_dir/geek2/university2/geek.txt')
except FileNotFoundError:
    print('Arquivo nao encontrado')

print("--------------------------------------------------")

# Excluir arquivos
# ATENÇÂO! Ao excluir um arquivo eles são excluídos permanentemente
try:
    os.remove('new_dir/geek2/university2/geek.txt')
    print('Arquivo removido')
except FileNotFoundError:
    print('Arquivo não encontrado')
# OBS.: Se o arquivo não existir será lançado um FileNotFoundError
# OBS.: Se você estiver no Windows e o arquivo estiver aberto será lançado um erro

# O comando os.remove() exclui um arquivo, caso seja passado um diretório, será lançado o erro IsADirectoryError
try:
    os.remove('new_dir/geek2/university2')
    print('Diretório removido')
except IsADirectoryError:
    print('Foi informado um diretório ao invés de um arquivo')
except FileNotFoundError:
    print('Diretório não encontrado')

# Remover um diretório
# rmdir() -> remover diretórios vazios
try:
    os.rmdir('templates')
    print('Diretório removido')
except OSError:
    print('O diretório não está vazio')

# OBS.: Se o diretório não existir será lançado um FileNotFoundError
# OBS.: Se o diretório não estiver vazio será lançado um OSError

# Remover toda a árvore de diretório vazios
try:
    os.removedirs('templates/geek/university')
    print('Diretório templates/geek/university foi removido')
except FileNotFoundError:
    print('Diretórios não encontrados')

try:
    os.removedirs('new_dir/geek2/university2')
    print('Diretórionew_dir/geek2/university2 foi removido')
except FileNotFoundError:
    print('Diretórios não encontrados')

print("--------------------------------------------------")

# Criar diretórios temporários

# Além do import do os, é necessário importar o tempfile
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    # input('Aperte uma tecla para continuar... O arquivo temporário será excluído.')

# OBS.: possívelmente o código acima não irá funcionar com Windows, pelo fato desse sistema
# trabalhar de forma diferente com arquivos temporários

print("--------------------------------------------------")

# Criar arquivos temporários

# OBS.: Em arquivos temporários só conseguimos escrever em binário
with tempfile.TemporaryFile() as tmp:
    # write(b'texto') -> converter a string em binário
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

# Sem o bloco with
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

# Usando o comando NamedTemporaryFile
arquivo = tempfile.NamedTemporaryFile()
print(f'Nome do arquivo temporário: {arquivo.name}')
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

print("--------------------------------------------------")

# Apagar arquivos e diretórios criados na aula
try:
    os.remove('arquivos/arquivo-teste1.txt')
    os.remove('arquivos/arquivo-teste2.txt')
    os.remove('arquivos/arquivo-teste3.txt')
    os.remove('arquivos/arquivo-teste4.txt')
    os.remove('python/arquivo-teste1.txt')
except FileNotFoundError:
    print('Arquivos não encontrados')

try:
    os.removedirs('python')
    os.removedirs('new_dir/geek2')
except FileNotFoundError:
    print('Diretório não encontrado')
