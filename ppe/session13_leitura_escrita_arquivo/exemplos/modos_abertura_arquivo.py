"""
Modos de abertura de arquivos

r -> abre o arquivo para leitura (padrão)
w -> abre o arquivo para escrita
x -> abre o arquivo para escrita, se o arquivo não existir caso contrário será lançado um FileExistsError
a -> abre o arquivo para escrita, adicionando o conteúdo SEMPRE ao final do arquivo.
     Se o arquivo não existir será criado. Não é possível controlar o cursor
+ -> abre o arquivo para atualização: leitura e escrita. Podemos controlar o cursor
"""

# Exemplo x
try:
    with open('arquivos/university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo.\n')
except FileExistsError:
    print('Arquivo já existe')

print("--------------------------------------------------")

# Exemplo a
with open('arquivos/frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

print("--------------------------------------------------")

# Adicionar conteúdo no inicio do arquivo
with open('arquivos/outro_arquivo.txt', 'r+') as arquivo:
    texto_anterior = arquivo.read()
    arquivo.seek(0)
    arquivo.write('Topo 1!\n')
    arquivo.write('Nova linha!\n')
    arquivo.write('Mais uma linha!\n')
    arquivo.write(texto_anterior)
