"""
Funções com parâmetro de entrada
 - Funções que recebem dados para serem processados dentro da mesma;

Diferença entre parâmetros e argumentos
 - Parâmetros são variáveis declaradas na definição de uma função
 - Argumentos são os dados passados durante a execução de uma função
"""


def quadrado(numero):
    return numero ** 2


print(f'O quadrado de 7 é: {quadrado(7)}')
print(f'O quadrado de 2 é: {quadrado(2)}')
print(f'O quadrado de 3 é: {quadrado(5)}')

print("--------------------------------------------------")


# Refatorando função cantar parabéns
def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de de vida')
    print(f'Viva o/a {aniversariante}!')


print(f'Cantar parabéns para o Marcos')
cantar_parabens("Marcos")
print()
print(f'Cantar parabéns para o Patricia')
cantar_parabens("Patricia")

print("--------------------------------------------------")
"""
Funções podem ter N parâmetros de entrada, ou seja, podem receber como entrada
em uma função quantos parâmetros forem necessários. Eles serão separados por vírgula.
"""


def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(f'Soma de 2 + 5 = {soma(2, 5)}')
print(f'Soma de 10 + 20 = {soma(10, 20)}')
print(f'Multiplicação de 4 * 5 = {multiplica(4, 5)}')
print(f'Multiplicação de 2 * 8 = {multiplica(2, 8)}')
print(f'Executando função outra(3, 2, Geek): {outra(3, 2, "Geek ")}')
print(f'Executando função outra(5, 4, Python): {outra(5, 4, "Python ")}')

# OBS.: Se informar um número errado de parâmetros ou argumentos, teremos erro de TypeError
print("--------------------------------------------------")


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


arg_nome = 'Felicity'
arg_sobrenome = 'Jones'

# A ordem dos parâmetros importa
print(nome_completo(arg_nome, arg_sobrenome))
print(nome_completo(arg_sobrenome, arg_nome))

# Argumentos nomeados (Keyword Arguments)
# Caso utilizamos os nomes do parâmetros ao informar os argumentos, podemos utilizar qualquer ordem
print(nome_completo(nome=arg_nome, sobrenome=arg_sobrenome))
print(nome_completo(sobrenome=arg_sobrenome, nome=arg_nome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))

print("--------------------------------------------------")


# Uma função pode receber qualquer tipo de dado como parâmetro
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


# Enviando uma lista
lista = [1, 2, 3, 4, 5, 6, 7]
print(f'Somando a lista: {soma_impares(lista)}')

# Enviando uma tupla
tupla = (1, 2, 3, 4, 5, 6, 7)
print(f'Somando a tupla: {soma_impares(tupla)}')
