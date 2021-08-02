"""
Funções de maior grandeza - Higher Order Functions (HOF)

O que isso significa?
  - Quando uma linguagem de programação tem suporte a HOF, indica que podemos ter funções
que retornam outras funções como resultado ou mesmo que podemos passar funções como argumentos
para outras funções e até mesmo criar variáveis do tipo de funções nos nossos programas.

Em Python as funções também são conhecidas como Cidadões de Primeira Classe, First Class Citizen
"""
# Difinir funções


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as funções
print(f'Somar: {calcular(4, 3, somar)}')
print(f'Somar: {calcular(4, 3, diminuir)}')
print(f'Somar: {calcular(4, 3, multiplicar)}')
print(f'Somar: {calcular(4, 3, dividir)}')

print("--------------------------------------------------")

# Nested Functions - Funções Aninhadas
"""
Em Python podemos ter funções dentro de funções, que são conhecidas por
Nested Functions ou Inner Functions (Funções Internas).
"""

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('Oi ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa


print(cumprimento('Mariana'))
print(cumprimento('Carlos'))
print(cumprimento('Camila'))
print(cumprimento('Gabriela'))

print("--------------------------------------------------")

# Retornar funções de outras funções


def faz_me_rir():
    def rir():
        return choice(('rs ', 'kkkkk ', 'hahaha '))
    return rir


rindo = faz_me_rir()
print(f'Tipo da variável rindo: {type(rindo)}')
print(rindo())


print("--------------------------------------------------")

# Inner functions podem acessar o escopo de funções mais externas.


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('rs', 'kkkkk', 'hahaha'))
        return f'{risada} {pessoa}'
    return dando_risada


rindo = faz_me_rir_novamente('Fernanda')
print(rindo())
print(rindo())
print(rindo())
