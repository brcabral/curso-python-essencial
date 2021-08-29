"""
Argumentos somente posicionais
"""

valor = '67.3'
print(float(valor))

# Em argumentos posicionais, não é possível usar parâmetros nomeados
# print(float(x=valor))

print("--------------------------------------------------")


def cumprimenta_v1(nome):
    return f'Olá {nome}'


print(cumprimenta_v1('Geek'))
print(cumprimenta_v1(nome='Geek'))


# Criando função somente posicionais
# Acrescentar uma barra ( / ) como um segundo argumento
# Todos os argumentos antes da barra será posicional
def cumprimenta_v2(nome, /):
    return f'Olá {nome}'


print()
print(cumprimenta_v2('Geek'))

# print(cumprimenta_v2(nome='Geek'))

print("--------------------------------------------------")


# Função com 2 parâmetros, sendo apenas o primeiro posicional
def cumprimenta_v3(nome, /, mensagem='Olá'):
    return f'{mensagem} {nome}'


print(cumprimenta_v3('Geek'))
print(cumprimenta_v3('Geek', mensagem='Hello'))
print(cumprimenta_v3('Felicity', 'Bem-vinda'))

print("--------------------------------------------------")


# Função com 2 parâmetros sendo ambos posicional
def cumprimenta_v4(nome, mensagem='Olá', /):
    return f'{mensagem} {nome}'


print(cumprimenta_v4('Geek'))
print(cumprimenta_v4('Felicity', 'Bem-vinda'))
# print(cumprimenta_v4('Geek', mensagem='Hello'))

print("--------------------------------------------------")


# Todos os argumentos após o asterisco precisam ser nomeados.
def cumprimenta_v5(*, nome):
    return f'Olá {nome}'


print(cumprimenta_v5(nome='Geek'))
# print(cumprimenta_v5('Geek'))

print("--------------------------------------------------")


# Mesclando o posicional e a obrigatoriedade de nomear os argumentos
def cumprimentar_v6(nome, /, mensagem1='Olá', *, mensagem2):
    return f'{mensagem1} {nome} {mensagem2}'


print(cumprimentar_v6('Geek', mensagem1='Hello', mensagem2='tenha um bom dia'))
print(cumprimentar_v6('Geek', mensagem2='tenha um bom dia'))
# print(cumprimentar_v6('Geek', 'Oi', 'Vamos'))
# print(cumprimentar_v6(nome='Geek', 'Oi', mensagem2='. Como vocês está?'))
