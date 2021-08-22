"""
Doctests
 - São testes que colocamos na docstring das funções/métodos Python
   - Para rodar um test do doctest
     -> python -m doctest -v nome_do_modulo.py
"""


# def soma(a, b):
#     """Soma os números a e b
#       >>> soma(1, 2)
#       3
#
#       >>> soma(4, 6)
#       10
#     """
#     return a + b


print("--------------------------------------------------")

# Aplicando TDD


# def duplicar(valores):
#     """Duplica os valores em uma lista
#     >>> duplicar([1, 2, 3, 4])
#     [2, 4, 6, 8]
#
#     >>> duplicar([])
#     []
#
#     >>> duplicar(['a', 'b', 'c'])
#     ['aa', 'bb', 'cc']
#
#     >>> duplicar([True, None])
#     Traceback (most recent call last):
#         ...
#     TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
#     """
#     return [2 * elemento for elemento in valores]


print("--------------------------------------------------")

# Erro inesperado


# def fala_oi():
#     """Fala oi
#       >>> fala_oi()
#       "oi"
#
#       >>> fala_oi()
#       'oi'
#     """
#     return "oi"


print("--------------------------------------------------")

# Mais um caso estranho
"""
Se colocar um espaço após o True, no Doctest, e executar o código no Pychar não dará erro, pois a 
ferramenta retira os espaços em branco após o fim do código. Já se o mesmo código for executado
via shell, por exemplo, ocorrerá o erro, pois o retorno estará esperando um espaço após o True
"""


def verdade():
    """Retorna verdade
      >>> verdade()
      True
    """
    return True
