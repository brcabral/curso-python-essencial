"""
Tipos complexos de dados em Python na prática
"""

nomes: list = ['Geek', 'University']
versoes: tuple = (3, 4, 7)
opcoes: dict = {'ar': True, 'banco_couro': True}
valores: set = {3, 4, 5, 6}

print(f'Nomes: {nomes}')
print(f'Versões: {versoes}')
print(f'Opções: {opcoes}')
print(f'Valores: {valores}')
print(__annotations__)

print("--------------------------------------------------")

# Declarando o type hiting dos valores de uma lista, tupla, dicionário ou set

from typing import Dict, List, Tuple, Set

nomes: List[str] = ['Geek', 'University']
versoes: Tuple[int, int, int] = (3, 4, 7)
opcoes: Dict[str, bool] = {'ar': True, 'banco_couro': True}
valores: Set[int] = {3, 4, 5, 6}

print(f'Nomes: {nomes}')
print(f'Versões: {versoes}')
print(f'Opções: {opcoes}')
print(f'Valores: {valores}')
print(__annotations__)
