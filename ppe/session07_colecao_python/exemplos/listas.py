"""
Listas
Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagem,
com a diferença de serem DINÂMICAS e também e aceitarem QUALQUER tipo de dado.

- Dinâmico:
  - Não possuem tamanho fixo, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado:
  - Não possuem tipo de dado fixo, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes []
As listas são mutáveis, ou seja, elas podem ser alteradas
"""
print(type([]))

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')
lista7 = ['Programação', 'em', 'Python', 'Essencial']
# Podemos colocar qualquer tipo de dado em uma lista, inclusive mesclando os tipos
lista8 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45345345345]

# Podemos checar se um determinado valor está contido na lista
num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

letra = 'e'
if letra in lista5:
    print(f'Encontrei a letra {letra}')
else:
    print(f'Não encontrei a letra {letra}')

print('--------------------------------------------------')

# Podemos ordenar uma lista
lista1.sort()
print(f'lista1 ordenada: {lista1}')

print('--------------------------------------------------')

# Podemos contar o número de ocorrências de um valor em uma lista
print(f'Quantas vezes o número 1 aparece na lista1: {lista1.count(1)}')
print(f'Quantas vezes a letra e aparece na lista5: {lista5.count("e")}')

print('--------------------------------------------------')

# Adicionar elementos em uma lista
"""
Com o append adicionamos apenas 1 elemento por vez no final da lista
"""
print(f'Lista1 atual: {lista1}')
print('Adicionando itens com append...')
lista1.append(42)
lista1.append('e')
lista1.append([8, 3, 1])  # Adiciona uma lista dentro da lista principal
print(f'Lista1 atualizada: {lista1}')

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])  # Adiciona os novos elementos como valores adicionais na lista principal
"""
Com o extend podemos adicionar apenas valores iteráveis a lista principal
Para adicionar um único elemento, usar o append
"""
print(f'Lista1 atualizada: {lista1}')

print('--------------------------------------------------')

# Podemos inserir um novo elemento na lista informando a posição do índice
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

print(f'Lista1 atual: {lista1}')
lista1.insert(2, 'Novo valor')
# O insert não substitui o valor atual, o mesmo será deslocado para o próximo índice da lista
print(f'Lista1 atualizada: {lista1}')

print('--------------------------------------------------')

# Podemos juntar duas listas
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

print(f'Lista1 atual {lista1}')
lista1.extend(lista2)
print(f'Lista1 atualizada {lista1}')

# Caso seja necessário juntar duas listas e manter as duas atuais inalteradas
# pode-se soma-las em uma nova variável
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista6 = lista1 + lista2
print(f'Lista6 {lista6}')

print('--------------------------------------------------')
# Podemos inverter uma lista
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

print(f'Lista1 atual {lista1}')
print(f'Lista2 atual {lista2}')

lista1.reverse()
lista2.reverse()
"""
Para reverter uma lista também é possível utilizando o slice
lista1[::-1]
lista2[::-1]
"""

print(f'Lista1 invertidas {lista1}')
print(f'Lista2 invertidas {lista2}')

print('--------------------------------------------------')
# Atribuindo uma lista a uma nova variável
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
print(f'Lista2 {lista2}')

"""
Copiando a lista via atribuição.
As listas são "compartilhadas", ou seja, se alterarmos qualquer uma delas a outra também será alterada

Esse método de cópia é conhecido como Shallow Copy (cópia rasa)
"""
lista6 = lista2

print(f'Lista6 {lista6}')

lista2.extend([50, 55, 57])
lista6.extend([70, 75, 77])

print(f'Lista2 {lista2}')
print(f'Lista6 {lista6}')

print('--------------------------------------------------')
# Podemos copiar uma lista
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
print(f'Lista2 {lista2}')

"""
Copiamos a lista com a função copy
As listas ficam totalmente independentes, ou seja, se alteramos os elementos de uma das lista,
a alteração não será refletida na outra.

Esse método de cópia é conhecido como Deep Copy (cópia profunda)
"""
lista6 = lista2.copy()

print(f'Lista6 {lista6}')

lista2.extend([50, 55, 57])
lista6.extend([70, 75, 77])

print(f'Lista2 {lista2}')
print(f'Lista6 {lista6}')

print('--------------------------------------------------')
# Contar a quantidade de elementos de uma lista
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))

print(f'Contem {len(lista1)} elementos na lista1')
print(f'Contem {len(lista2)} elementos na lista2')
print(f'Contem {len(lista3)} elementos na lista3')
print(f'Contem {len(lista4)} elementos na lista4')

print('--------------------------------------------------')
# Podemos remover o último elemento de uma lista
lista5 = list('Geek University')
print(f'Lista5 atual {lista5}')

# O pop remove o último elemento e também retorna o valor removido
num_removido = lista5.pop()
print(f'Numero removido: {num_removido}')
print(f'Lista5 atualizada {lista5}')

# Também podemos remover um elemento pelo índice com o pop
# Obs.: Os elementos a direita deste índice serão deslocados a esquerda
# Obs.: Se não houver elemento no índice informado, teremos o erro IndexError
lista5.pop(2)
print(f'Lista5 atualizada {lista5}')

print('--------------------------------------------------')
# Podemos remover todos os elementos de uma lista
lista5 = list('Geek University')
print(f'Lista5 atual {lista5}')
lista5.clear()
print(f'Lista5 atualizada {lista5}')

print('--------------------------------------------------')
# Podemos multiplicar os elementos de uma lista, nela mesmo
nova_lista = [1, 2, 3]
print(f'nova_lista atual {nova_lista}')
# nova_lista = nova_lista * 3
nova_lista *= 3
print(f'nova_lista atualizada {nova_lista}')

print('--------------------------------------------------')
# Converter uma string para uma lista

# Exemplo 01
curso = 'Programação em Python Essencial'
print(f'variavel curso: {curso}')
# Por padrão, o split separa os elementos da string pelo espaço entre as palavras
curso = curso.split()
print(f'variavel curso: {curso}')

# Exemplo 01
curso = 'Programação,em,Python,Essencial'
print(f'variavel curso: {curso}')
curso = curso.split(',')
print(f'variavel curso: {curso}')

print('--------------------------------------------------')
# Converter uma lista em uma string
lista7 = ['Programação', 'em', 'Python', 'Essencial']
print(f'Lista7 {lista7}')

curso_espaco = ' '.join(lista7)
print(f'variavel curso_espaco: {curso_espaco}')

curso_hifen = '-'.join(lista7)
print(f'variavel curso_hifen: {curso_hifen}')

print('--------------------------------------------------')
lista8 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45345345345]
print(f'lista8 {lista8}')

print('--------------------------------------------------')
# Imprimindo uma lista mista
lista8 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45345345345]
print(f'lista8 {lista8}')

print('--------------------------------------------------')
# Contar a quantidade de um mesmo elemento em uma lista
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
print(f'lista2 {lista2}')
print(f'Há {lista2.count("e")} letras E em na lista')
print(f'Há {lista2.count("i")} letras I em na lista')

print('--------------------------------------------------')
# Iterando sobre listas com for e while
"""
carrinho = []
produto = ''

while produto != 'sair':
    produto = input('Adicione um produto na lista ou digite "sair" para sair: ')
    if produto != 'sair':
        carrinho.append(produto)

print()
print("Lista de produtos selecionado")
for p in carrinho:
    print(p)
"""

print('--------------------------------------------------')
# Acessamos os elementos de uma lista de forma indexada

#           0         1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(f'cores {cores}')

print(f'posição 0: {cores[0]}')  # verde
print(f'posição 1: {cores[1]}')  # amarelo
print(f'posição 2: {cores[2]}')  # azul
print(f'posição 3: {cores[3]}')  # branco

# Podemos também acessar a lista de forma inversa
"""
Para entender melhor o índice negativo, pense na lista como um círculo,
onde último elemento da lista é sucedido pelo primeiro elemento.
"""
print()
print('Acessando com a lista de forma inversa')
print(f'posição -1: {cores[-1]}')  # branco
print(f'posição -2: {cores[-2]}')  # azul
print(f'posição -3: {cores[-3]}')  # amarelo
print(f'posição -4: {cores[-4]}')  # verde

print('--------------------------------------------------')
# Gerar indice em um for
cores = ['verde', 'amarelo', 'azul', 'branco']

for indice, cor in enumerate(cores):
    print(indice, cor)

print('--------------------------------------------------')
# Encontrar o índice de um elemento na lista
# Obs.: Caso não tenha o elemento procurado na lista, será apresentado um erro (ValueError)
cores = ['verde', 'amarelo', 'azul', 'branco', 'vermelho', 'verde', 'preto', 'branco', 'azul']

# Qual indice da lista está a cor azul?
print(f'Índice da cor azul: {cores.index("azul")}')

# Qual indice da lista está a cor vermelho?
print(f'Índice da cor vermelho: {cores.index("vermelho")}')

# Qual indice da lista está a cor amarelo?
# Obs.: Em caso de elementos duplicados, retorna o índice do primeiro elemento encontrado
print(f'Índice da cor verde: {cores.index("verde")}')

# Busca a cor verde a partir do índice x (no ex. 1)
print(f'Índice da cor verde a partir do índice 1: {cores.index("verde", 1)}')

# Busca a cor branco a com o índice x e y (no ex.: 2 e 6)
print(f'Índice da cor branco entre 2 e 6: {cores.index("branco", 2, 6)}')

print('--------------------------------------------------')
# Trabalhando com slice em listas
# lista[inicio:fim:passo]

lista = [1, 2, 3, 4, 5]
print(f'lista: {lista}')
print(f'lista completa: {lista[::]}')
print(f'lista iniciando no indice 1: {lista[1:]}')
print(f'lista iniciando no indice 2: {lista[2:]}')
print(f'lista até o elemento de indice 2: {lista[:2]}')
print(f'lista até o elemento de indice 3: {lista[:3]}')
print(f'lista iniciando no indice -3: {lista[-3:]}')
print(f'lista iniciando no indice 2, até o -2: {lista[2:-2]}')
print(f'lista iniciando no indice 1, até o fim, com intervalo de 2 números: {lista[1::2]}')
print(f'lista iniciando no indice 1, até o indice 3, com intervalo de 2 números: {lista[1:3:2]}')
print(f'lista completa com passo negativo (inverte a lista): {lista[::-1]}')

print('--------------------------------------------------')
# Inverterndo valores em uma lista
nomes = ['Geek', 'University']
print(f'lista nomes atual {nomes}')
nomes[0], nomes[1] = nomes[1], nomes[0]
print(f'lista invertida manualmente {nomes}')

nomes = ['Geek', 'University', 'Programação', 'Python']
print(f'lista nomes atual {nomes}')
nomes.reverse()
print(f'lista invertida com reverse {nomes}')

print('--------------------------------------------------')
# Soma*, valor máximo*, valor mínimo*, tamanho
# * Se os valores forem todos inteiros ou reais
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

print(f'Soma da lista1: {sum(lista1)}')
print(f'Maior valor da lista1: {max(lista1)}')
print(f'Menor valor da lista1: {min(lista1)}')
print(f'Tamanho da lista1: {len(lista1)}')

print('--------------------------------------------------')
# Transformar uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(f'lista atual: {lista}')
print(f'Tipo da variável lista = {type(lista)}')
print()

tupla = tuple(lista)
print(f'lista atual: {tupla}')
print(f'Tipo da variável tupla = {type(tupla)}')

print('--------------------------------------------------')
# Desempacotamento de lista
lista = [1, 2, 3]
print(f'lista atual: {lista}')

num1, num2, num3 = lista

print(f'Numero 1: {num1}')
print(f'Numero 2: {num2}')
print(f'Numero 3: {num3}')

"""
OBS.: Se houver um número diferente entre os elementos da lista e a quantidade de variáveis
será lançado um erro (ValueError)
"""
