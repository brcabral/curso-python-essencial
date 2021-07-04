"""
Funções com retorno

OBS 1.: Quando um função não retorna nenhum valor, o retorno é None
OBS 2.: Para funções que retornam valores, devem usar a palavra reservada return para indicar o valor retornado
OBS 3.: Não precisamos necessariamente criar uma variável para receber o retorno de uma função.
        Podemos passar a execução da função para outra função.
"""
numeros = [1, 2, 3]
print(f'O número excluído foi: {numeros.pop()}')
print(f'Lista de números: {numeros}')

print("--------------------------------------------------")


def quadrado_de_7():
    print(7 * 7)


# Quando executamos a função, será exibido o valor 49
# Porém o valor não está sendo retornado pela função, mas sendo impressa por ela
quadrado_de_7()

print("--------------------------------------------------")


# Refatorando a função quadrado_de_7 para retornar um valor
def quadrado_de_sete():
    return 7 * 7


# Criamos uma variável para receber o retorno da função
resultado = quadrado_de_sete()
print(f'O resultado da função quadrado_de_sete é: {resultado}')

# Executando a função direta, dentro do print()
print(f'Executando a função quadrado_de_sete: {quadrado_de_sete()}')

print("--------------------------------------------------")


# Refatorando função diz_oi para retornar um valor


def diz_oi():
    return 'Oi '


nome = 'Pedro'
print(f'Executando função diz_oi: {diz_oi()}!')
print(f'Executando função diz_oi: {diz_oi() + nome}!')

print("--------------------------------------------------")
"""
Sobre o return
 - Ele finaliza a função, ou seja, ele finaliza a execução da função
 - Podemos ter, em uma função, diferentes returns
 - Uma função pode retornar qualquer tipo de dado, pode até retonar múltiplos valoes
"""


# Exemplo 1 -> finaliza a função
def novo_diz_oi():
    print('Estou sendo executado antes o retorno!')
    return 'Oi!'
    print('Estou sendo executado após o retorno!')


print(novo_diz_oi())

print("--------------------------------------------------")


# Exemplo 2 -> diferentes returns
def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(f'Executando a função nova_funcao(): {nova_funcao()}')

print("--------------------------------------------------")


# Exemplo 3 -> retornar multiplos valores
def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()
print(f'Primeiro valor: {num1}')
print(f'Segundo valor: {num2}')
print(f'Terceiro valor: {num3}')
print(f'Quarto valor: {num4}')
print(f'Executando a função outra_funcao: {outra_funcao()}')

print("--------------------------------------------------")
# Função para jogar cara ou coroa
from random import random


def cara_coroa():
    # random() -> Gera um número pseudo randômico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


for i in range(1, 11):
    print(f'{i}ª jogada: {cara_coroa()}')
