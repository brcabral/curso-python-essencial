"""
Entendendo o **kwargs
 - O *kwargs é um parâmetro, como outro qualquer, isso significa que ele pode ter qualquer nome
desde que começe com duplo asterisco.
 - Mas por convenção, utilizamos *kwargs para definí-lo
 - Diferente do *args que coloca os valores em uma tupla, o **kwargs exige que utilizamos
parâmetros nomeados e transforma esses parâmetros extras em um dicinário
"""


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS.: Assim como o *args, o **kwargs pode receber 0..N parâmetros
cores_favoritas()
cores_favoritas(geek='navy')
cores_favoritas(camila='rosa', fabio='preto')

print("--------------------------------------------------")


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f'{kwargs["geek"]} Geek!'
    return 'Não tenho certeza quem você é...'


print(f'executando a função cumprimento_especial(): {cumprimento_especial()}')
print(f'executando a função cumprimento_especial(geek="Python"): {cumprimento_especial(geek="Python")}')
print(f'executando a função cumprimento_especial(geek="Oi"): {cumprimento_especial(geek="Oi")}')
print(f'executando a função cumprimento_especial(geek="especial"): {cumprimento_especial(geek="especial")}')

print("--------------------------------------------------")
"""
As funções podem ter os seguintes tipos de parâmetros e respeitar a seguinte ordem:  
 - Parâmetros obrigatórios
 - *args
 - Parâmetros default (não obrigatórios)
 - **kwargs
"""


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro(a)')
    else:
        print('Casado(a)')
    print(kwargs)
    print()


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

print("--------------------------------------------------")
# Entendendo porque é importante manter a ordem dos parâmetros na declaração


def mostra_info_ordem_correta(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


def mostra_info_ordem_incorreta(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info_ordem_correta(1, 2, 3, sobrenome='University', cargo='Instrutor'))
print(mostra_info_ordem_incorreta(1, 2, 3, sobrenome='University', cargo='Instrutor'))
# Perceba que o a tupla ficou vazia e o 3 foi atribuído ao parâmetro instrutor

print("--------------------------------------------------")
# Desempacotar com **kwargs


def mostra_nome(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}'


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}
print(mostra_nome(**nomes))
