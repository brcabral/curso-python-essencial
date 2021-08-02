"""
Decorators com diferentes assinaturas
  Quando as funções tiverem quantidade de parâmetos diferentes, usamos o padrão de projeto Decorator Pattern
"""


# def gritar(funcao):
#     def aumentar(nome):
#         return funcao(nome).upper()
#     return aumentar


# Refatorando para receber diferente quantidades de parâmetros
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def pedido(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'


print(saudacao('Ana Maria'))
print(pedido('Picanha', 'Batata frita'))

print("--------------------------------------------------")


# Decorators com argumentos
def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


# Posso informar quantos pratos quiser, porém o primeiro precisa ser pizza
@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


# O primeiro num1 tem que ser igual à 10
@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


print(soma_dez(10, 12))
print(soma_dez(12, 10))

print()

print(comida_favorita('pizza', 'lasanha', 'churrasco'))
print(comida_favorita('churrasco', 'lasanha'))
