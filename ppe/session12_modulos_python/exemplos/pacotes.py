"""
Pacotes

Módulo -> É um arquivo Python que tem uma ou mais funções para ser utilizada;
Pacote -> É um diretório contendo uma coleção de módulos;

OBS.: Nas versões 2.x do Python, dentro de um pacote deve conter um arquivo chamado __init__.py
Nas versões 3.x, não é mais obrigatório a utilização deste arquivo, porém normalmente ainda é
utilizado para manter compatibilidade.
"""

from geek import geek1, geek2
from geek.university import geek3, geek4
from geek.geek1 import funcao1

print(f'Valor de PI: {geek1.pi}')
print(f'Executando funcao1: {geek1.funcao1(4, 6)}')

print(f'Valor de curso: {geek2.curso}')
print(f'Executando funcao2: {geek2.funcao2()}')

print(f'Executando funcao3: {geek3.funcao3()}')
print(f'Executando funcao4: {geek4.funcao4()}')

print(f'Executando funcao1: {funcao1(6, 9)}')
