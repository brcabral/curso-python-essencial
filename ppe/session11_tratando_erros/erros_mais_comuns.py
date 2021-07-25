"""
Erros mais comuns em Python

É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução
do nosso código.

OBS.: Exceptions e Errors são sinônimos em programação
"""

# 1 - SyntaxError
"""
SyntaxError -> Ocorre quando o Python encontra uma erro de sintaxe. Ou seja, o código escrito
tem comandos não reconhecido pela linguagem Python

a)
def funcao:
    print('Geek University')

b)
None = 1
def = 1
"""

# 2 - NameError
"""
NameError -> Ocorre quando uma variável ou função não foi definida.

a)
print(geek)

b)
geek()
"""

# 3 - TypeError
"""
TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

a)
print(len(5))

b)
print('Geek' + [])
print('Geek' + 4)
"""

# 4 - IndexError
"""
IndexError -> Ocorre quando tentamos acessar um elemento indexado utilizando um índice inválido

a)
lista = ['Geek']
print(lista[2])
print(lista[0][10])
"""

# 5 - ValueError
"""
ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo
correto mas valor inapropriado.

a)
print(int('Geek'))
"""

# 6 - KeyError
"""
KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

a)
dic = {'a': 1}
print(dic['b'])
"""

# 7 - AttributeError
"""
AttributeError -> Ocorre quando uma variável não tem um atributo/função

a)
tupla = (11, 2, 31, 4)
tupla.sort()
print(tupla)

"""

# 8 - IdentationError
"""
IdentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

a)
def nova():
print('Geek')

b)
for i in range(10):
i + 1

c)
if 1 == 1:
  print('Entrou no if')
    print('Teste')
"""
