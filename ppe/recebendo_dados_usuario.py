"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
 - Aspas simples;
 - Aspas duplas;
 - Aspas simples triplas;
 - Aspas duplas triplas;

Exemplo:
 - Aspas simples -> 'Python'
 - Aspas duplas -> "Python"
 - Aspas simples triplas -> '''Python'''
"""
# - Aspas duplas triplas -> """Python"""

# print("Qual seu nome?")
# nome = input()

nome = input("Qual seu nome? ")

# Exemplo de print 'antigo' 2.x
# print('Seja bem vindo(a) %s.' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem vindo(a) {0}.'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem vindo(a) {nome}.')

# print('Qual sua idade?')
# idade = input()

#idade = input("Qual sua idade? ")
idade = int(input("Qual sua idade? "))

# Exemplo de print 'antigo' 2.x
# print('%s tem %s anos.' % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('{0} tem {1} anos.'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'{nome} tem {idade} anos.')

# print(f'{nome} nasceu em {2021 - int(idade)}')
print(f'{nome} nasceu em {2021 - idade}')
