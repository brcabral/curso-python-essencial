"""
Conjuntos
 - Conjuntos em qualquer linguagem de programação, estamos fazendo referência a Teoria dos Conjuntos da Matemática
 - Em Python, os conjuntos são chamados de Sets

Da mesmo forma que na matemática os Sets (conjuntos):
 - Não possuem valores duplicados;
 - Não possuem valores ordenados;
 - Os elementos não são acessados por index, ou seja, não são indexados

Conjuntos são bons para se utilizar quando:
 - Precisamos armazenar elementos sem se importar com a ordenação deles
 - Não precisamos se preocupar com chaves, valores e itens duplicados

Os conjuntos (sets) são representadas por chaves {}

Diferença entre Conjuntos e Dicionários em Python:
 - Um dicinário tem chave/valor;
 - Um conjunto tem apenas valor;
"""
# Definindo um conjunto
# Ao criar um conjunto, se houver valores repetidos, esses serão ignorados sem gerar erros.

# Forma 1
conjunto = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3, 6, 1})
print(f'conjunto: {conjunto}')
print(f'Tipo do conjunto = {type(conjunto)}')

# Forma 2 - Mais comum
conjunto = {1, 2, 3, 4, 5, 5}
print(f'conjunto: {conjunto}')
print(f'Tipo do conjunto = {type(conjunto)}')

# Gerando conjunto através de uma string
conjunto = set('Geek University')
print(f'conjunto: {conjunto}')

# Gerando um conjunto através de uma lista
lista = [1, 2, 3, 4, 5, 6, 4, 2, 7, 3]
conjunto = set(lista)
print(f'conjunto: {conjunto}')

# Gerando um conjunto através de uma tupla
tupla = (1, 3, 4, 8, 6, 4, 2, 7, 3, 9)
conjunto = set(tupla)
print(f'conjunto: {conjunto}')

# Podemos verificar se um determinado elemento está contido no conjunto
if 3 in conjunto:
    print('Tem o 3')
else:
    print('Não tem o 3')

print('--------------------------------------------------')
# Conjuntos não tem elementos duplicados e não respeita a ordem declarada

# Listas aceitam valores duplicados
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados
tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionários não aceitam chaves duplicadas
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

print('--------------------------------------------------')
# Como nas demais coleções em Python, podemos colocar qualquer tipo de dados misturados em Sets
conjunto = {3, 'b', True, 34.22, 'a', 44, 1}
print(f'conjunto: {conjunto}')

print('--------------------------------------------------')
# Iterar sobre Sets
conjunto = {3, 'b', True, 34.22, 'a', 44, 1}

for valor in conjunto:
    print(valor)

print('--------------------------------------------------')
# Usos interessantes com Sets
"""
Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu
e os visitantes informam manualmente a cidade de onde vieram.

Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos aedicionar
novos elementos e ter repetição.
"""

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(f'Conjunto cidades: {cidades}')
print(f'Houve quantos visitantes: {len(cidades)}')

# Agora precisamos saber quantas cidades distintas tiveram
cidades_distintas = set(cidades)
print(f'Conjunto cidades_distintas: {cidades_distintas}')
print(f'Houve quantas cidades distintas: {len(cidades_distintas)}')

print('--------------------------------------------------')
# Adicionando elementos em um conjunto
conjunto = {1, 2, 3}
print(f'conjunto: {conjunto}')

conjunto.add(4)
conjunto.add(4)  # Duplicidade não gera erro, simplemente não é adicionado
conjunto.add(5)
print(f'conjunto: {conjunto}')

print('--------------------------------------------------')
# Remover elementos de um conjunto
conjunto = {1, 2, 3, 4}
print(f'conjunto: {conjunto}')

# Forma 1
# OBS.: Caso o valor informado não exista, será apresentado o erro KeyError
# Nenhum valor é retornado ao excluir um elemento
conjunto.remove(3)
print(f'conjunto após remove: {conjunto}')

# Forma 2
# OBS.: Caso o valor informado não exista, nenhum erro é gerado
conjunto.discard(2)
print(f'conjunto após discard: {conjunto}')

print('--------------------------------------------------')
# Copiando um conjunto
"""
Assim como nas listas podemos copiar a lista por Shallow Copy Deep Copy
 - Shallow = Cópia por atribuíção (dicionários compartilhados)
 - Deep = Cópia através do método copy (dicionários independentes)
"""
numeros = {1, 2, 3, 4, 5, 6}
print(f'Conjunto numeros: {numeros}')

# copia = numeros
copia = numeros.copy()
print(f'Conjunto copia: {copia}')

copia.add(7)
print(f'Conjunto numeros: {numeros}')

print('--------------------------------------------------')
# Removendo todos os elementos de um conjunto

numeros = {1, 2, 3, 4, 5, 6}
print(f'Conjunto numeros: {numeros}')

numeros.clear()
print(f'Conjunto numeros: {numeros}')

print('--------------------------------------------------')
# Métodos matemáticos de Conjuntos
"""
Imagina que temos dois conjuntos contendo:
 - Estudantes do curso de Python
 - Estudantes do curso de Java
"""
estudantes_python = {'Macos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}
print(f'Conjunto estudantes_python: {estudantes_python}')
print(f'Conjunto estudantes_java: {estudantes_java}')

# Veja que alguns alunos que estudam Python também estudam Java
# Precisamos gerar um conjunto com nomes únicos dos estudantes

# Forma 1 - Utilizando union
unicos1 = estudantes_python.union(estudantes_java)
print(f'Conjunto unicos1: {unicos1}')

# Forma 2 - Utilizando o caractere pipe (|)
unicos2 = estudantes_python | estudantes_java
print(f'Conjunto unicos2: {unicos2}')

# Gerar um conjunto de estudantes que estão em ambos os cursos
# Forma 1 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(f'Conjunto ambos1: {ambos1}')

# Forma 2 - Utilizando o caractere E comercial (&)
ambos2 = estudantes_python & estudantes_java
print(f'Conjunto ambos2: {ambos2}')

# Gerar um conjunto de estudantes de um curso que não estão no outro
so_python = estudantes_python.difference(estudantes_java)
print(f'Conjunto so_python: {so_python}')

so_java = estudantes_java.difference(estudantes_python)
print(f'Conjunto so_java: {so_java}')

print('--------------------------------------------------')
# Soma*, valor máximo*, valor mínimo*, tamanho
# * Se os valores forem todos inteiros ou reais
conjunto = {1, 2, 3, 4, 5, 6}

print(f'Soma do conjunto: {sum(conjunto)}')
print(f'Maior valor do conjunto: {max(conjunto)}')
print(f'Menor valor do conjunto: {min(conjunto)}')
print(f'Tamanho do conjunto: {len(conjunto)}')
