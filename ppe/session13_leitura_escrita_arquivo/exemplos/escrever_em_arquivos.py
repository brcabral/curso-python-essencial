"""
Escrevendo em arquivos
  Para escrever dados em um arquivo, devemos abrir o arquivo e depois usar a função write().
Essa função recebe uma string como parâmetro, caso contrário teremos um TypeError

  Ao abrir um arquivo para leitura, não podemos escrever nele.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo

  Ao abrir um arquivo para escrita, se o arquivo não existir ele será criado,
caso ele já exista, o anterior será apagado e um novo será criado.
Dessa forma o conteúdo do arquivo anterior será perdido.
"""

# Para abrir o arquivo no modo escrita, basta passar a letra w como parâmetro
with open('arquivos/novo_arquivo.txt', 'w') as arquivo:
    arquivo.write('Novos dados\n')
    arquivo.write('Outros podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Mais esta é a último linha.\n')

print("--------------------------------------------------")

arquivo = open('arquivos/mais.txt', 'w')
arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto')
arquivo.close()

print("--------------------------------------------------")

with open('arquivos/geek.txt', 'w') as arquivo:
    arquivo.write('Geek ' * 1000)

print("--------------------------------------------------")

# Podemos usar o writelines() para passar uma lista a ser escrita no arquivo
gatos = ['Uni\n', 'Gracinha\n', 'Kinder\n']

with open('arquivos/gatos.txt', 'w') as arquivo:
    arquivo.writelines(gatos)
