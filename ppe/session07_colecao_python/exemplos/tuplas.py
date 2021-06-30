"""
Tuplas

Tuplas são bastante parecidas com listas.
Existem basicamente duas diferenças

1 - As tuplas são representadas por parênteses ()
2 - As tuplas são imutáveis: Isso significa que ao criar uma tupla ele não muda.
Toda operação em uma tupla gera uma nova tupla.
"""

"""
Apesar das tuplas serem representadas por parênteses,
para definirmos uma tupla é necessário que os elementos sejam separados por vírgula.
Independentemente se os elementos estão ou não entre parênteses.

Outra forma de criar uma tupla é utilizando o método tuple()
"""
# Isso é uma tupla
tupla1 = (1, 2, 3, 4, 5, 6)
print(f'tupla1: {tupla1}')
print(f'Tipo da variável tupla1 = {type(tupla1)}')

# Isso é uma tupla
tupla2 = 1, 2, 3, 4, 5, 6
print(f'tupla2: {tupla2}')
print(f'Tipo da variável tupla2 = {type(tupla2)}')

# Isso não é uma tupla
tupla3 = (4)
print(f'tupla3: {tupla3}')
print(f'Tipo da variável tupla3 = {type(tupla3)}')

# Isso é uma tupla
tupla4 = (4,)
print(f'tupla4: {tupla4}')
print(f'Tipo da variável tupla4 = {type(tupla4)}')

# Isso é uma tupla
tupla5 = 4,
print(f'tupla5: {tupla5}')
print(f'Tipo da variável tupla5 = {type(tupla5)}')

# Isso é uma tupla
tupla6 = tuple('Geek University')
print(f'tupla6: {tupla6}')
print(f'Tipo da variável tupla6 = {type(tupla6)}')

print('--------------------------------------------------')
# Podemos gerar uma tupla a partir de um range
tupla = tuple(range(11))
print(f'tupla: {tupla}')

print('--------------------------------------------------')
# Desempacotamento de tupla

tupla = ('Geek University', 'Programação em Python')
escola, curso = tupla
print(f'escola: {escola}')
print(f'curso: {curso}')

print('--------------------------------------------------')
# Métodos para adição e remoção de elementos em tuplas não existem,
# pois as tuplas são imutáveis.
print('Não é possível adicionar e remover elementos de uma tupla.')

print('--------------------------------------------------')
# Soma*, valor máximo*, valor mínimo*, tamanho
# * Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6, 7.0)
print(f'Soma da tupla: {sum(tupla)}')
print(f'Maior valor da tupla: {max(tupla)}')
print(f'Menor valor da tupla: {min(tupla)}')
print(f'Tamanho da tupla: {len(tupla)}')

print('--------------------------------------------------')
# Concatenação de tuplas

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
print(f'tupla1: {tupla1}')
print(f'tupla2: {tupla2}')
print(f'tupla1 + tupla2: {tupla1 + tupla2}')
print(f'tupla1: {tupla1}')
print(f'tupla2: {tupla2}')

# Tuplas são imutáveis, mas podemos sobrescrever seus valores
tupla1 = tupla1 + tupla2
print(f'tupla1 concatenada com a tupla2: {tupla1}')

print('--------------------------------------------------')
# Verificar se determinado elemento está na tupla
tupla = tuple(range(1, 11))
print(f'O número 4 está na tupla: {4 in tupla}')
print(f'O número 7 está na tupla: {7 in tupla}')
print(f'O número 15 está na tupla: {15 in tupla}')

print('--------------------------------------------------')
# Iterando sobre uma tupla
tupla = tuple(range(5, 11))

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(f'valores da tupla {indice} -> {valor}')

print('--------------------------------------------------')
# Contando quantas vezes um elemento aparece em uma tupla

tupla = ('a', 'b', 'b', 'c', 'a', 'd', 'e', 'f', 'b', 'd', 'a', 'e')

print(f'Quantas vezes a letra b aparece na tupla: {tupla.count("b")}')
print(f'Quantas vezes a letra a aparece na tupla: {tupla.count("c")}')
print(f'Quantas vezes a letra e aparece na tupla: {tupla.count("e")}')

print('--------------------------------------------------')
# Dicas na utilização de tuplas
# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados em uma coleção

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
         'Outubro', 'Novembro', 'Dezembro')
print(f'meses do ano {meses}')

# O acesso aos elementos de uma tupla também é semelhante a de uma lista
print(f'Mês que está no índice 5: {meses[5]}')

# Verificar em qual índice um elemento está na tupla
print(f'Índice do mês Agosto: {meses.index("Agosto")}')

print('--------------------------------------------------')
# Trabalhando com slice em tuplas
# lista[inicio:fim:passo]

print(f'Todos os meses: {meses}')
print(f'Os cinco primeiros meses: {meses[:5]}')
print(f'A partir do oitavo mês até o fim: {meses[8:]}')
print(f'Todos os meses, indo de 2 em 2: {meses[::2]}')

print('--------------------------------------------------')
# Copiando tuplas
tupla = (1, 2, 3, 4)
print(f'tupla: {tupla}')

nova = tupla
print(f'tupla: {tupla}')
print(f'nova tupla: {nova}')

tupla = (10, 11, 12)
print(f'tupla (após alterar o valor da tupla): {tupla}')
print(f'nova (após alterar o valor da tupla): {nova}')

"""
Por que utilizar tuplas?
 - Tuplas são mais rápidas do que as listas
 - Tuplas deixam o código mais seguro
   - Trabalhar com elementos imutáveis traz mais segurança para o código
"""
