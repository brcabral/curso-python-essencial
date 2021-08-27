"""
Tipos em comentários
"""

import math


def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio


print(f'Função circunferencia: {circunferencia(8)}')

print("--------------------------------------------------")


def cabecalho1(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a '+texto
    else:
        return 'b '+texto


print("--------------------------------------------------")


def cabecalho2(
        texto,  # type: str
        alinhamento=True  # type: bool
):  # type: (...) -> str
    if alinhamento:
        return 'a '+texto
    else:
        return 'b '+texto


print("--------------------------------------------------")

nome = 'Geek University'  # type: str
