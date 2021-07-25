"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código.
Previnindo assim que o programa para de funcionar e o usuário receba mensagens
de erro inesperada.
"""

# Exemplo 1 - Tratando um erro genérico
try:
    geek()
except:
    print('Deu algum erro')

try:
    len(5)
except:
    print('Deu algum erro')

# OBS.: Tratar erro de forma genérica não é a melhor forma de tratamento de erro.
# O ideal é SEMPRE tratar de forma específica
print("--------------------------------------------------")

# Exemplo 2 - Tratando um erro especifico
try:
    geek()
except NameError:
    print('Você está chamando uma função inexistente')

try:
    len(5)
except TypeError:
    print('Você está passando um parâmetro inválido para a função')

print("--------------------------------------------------")

# Exemplo 3 - Tratando um erro especifico com detalhes do erro
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o erro: {err}')

print("--------------------------------------------------")

# Exemplo 4 - Tratando mais de um erro
try:
    # len(5)
    # geek()
    print('Geek'[9])
except NameError as erra:
    print(f'NameError: {erra}')
except TypeError as errb:
    print(f'TypeError: {errb}')
except:
    print(f'Deu um erro diferente')

print("--------------------------------------------------")


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {'nome': 'Geek'}
print(pega_valor(dic, 'nome'))
print(pega_valor(dic, 'game'))
print(pega_valor(7, 'nome'))
print(pega_valor(dic, 7))
