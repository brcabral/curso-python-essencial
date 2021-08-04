"""
Preservando metadatas (metadados) com wraps

Metadado
  - São dados intrínseca (dados não visíveis) em arquivos

Wraps
  - São funções que envolvem elementos com diversas finalidades
  - Preservam o metadado das funções
"""


# Exemplo do problema
def ver_log(funcao):
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando a função {funcao.__name__}')
        print(f'A documentação da função: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Somar dois números"""
    return a + b


# print(soma(10, 30))
print(soma.__name__)
print(soma.__doc__)

print("--------------------------------------------------")

# Resolendo o problema

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando a função {funcao.__name__}')
        print(f'A documentação da função: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Somar dois números"""
    return a + b


# print(soma(10, 30))
print(soma.__name__)
print(soma.__doc__)
