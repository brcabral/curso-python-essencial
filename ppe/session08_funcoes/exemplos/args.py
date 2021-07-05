"""
Entendendo o *args
 - O *args é um parâmetro, como outro qualquer, isso significa que ele pode ter qualquer nome
desde que começe com asterisco.
 - Mas por convenção, utilizamos *args para definí-lo

Mas o que é o *args?
 - O parâmetro *args utilizado em uma função, coloca os valores extras informados
como entrada em uma tupla.
"""


def soma_tres_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(f'executando a função soma_tres_numeros(4, 6, 8): {soma_tres_numeros(4, 6, 8)}')

print("--------------------------------------------------")
# Trabalhando com *args


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não tenho certeza quem você é...'


print(f'executando a função verifica_info(): {verifica_info()}')
print(f'executando a função verifica_info(1, True, "University", "Geek"): {verifica_info(1, True, "University", "Geek")}')
print(f'executando a função verifica_info(1, "University", 3.145): {verifica_info(1, "University", 3.145)}')

print("--------------------------------------------------")


def soma_todos_numeros(nome, *args):
    """
    Retorna a soma de todos os números passado como parâmetro no *args
    :param nome: parâmetro obrigatório
    :param args: parâmetro opcional, pode ser passado 0..N números
    :return: retorna a soma de todos os números passado
    """
    return sum(args)  # sum -> função que soma todos os valores de uma tupla


print(f'executando a função soma_todos_numeros(): {soma_todos_numeros("Python")}')
print(f'executando a função soma_todos_numeros(1): {soma_todos_numeros("Python", 1)}')
print(f'executando a função soma_todos_numeros(2, 3): {soma_todos_numeros("Python", 2, 3)}')
print(f'executando a função soma_todos_numeros(2, 3, 4): {soma_todos_numeros("Python", 2, 3, 4)}')
print(f'executando a função soma_todos_numeros(3, 4, 5, 6): {soma_todos_numeros("Python", 3, 4, 5, 6)}')

numeros = [1, 2, 3, 4, 5, 6, 7]
# A chamada abaixo vai gerar um TypeError, pois ele não permite enviar uma lista como parâmetro para o args
# print(f'executando a função soma_todos_numeros(): {soma_todos_numeros("Python", numeros)}')

# Porém podemos envair uma lista desempacotando ela
"""
O asterisco antes da variável serve para informarmos ao Python que estamos passando
como argumento uma coleção de dados. Por isso ele precisará desempacotar os dados
antes de utilizá-los
"""
print(f'executando a função soma_todos_numeros(*numeros): {soma_todos_numeros("Python", *numeros)}')
