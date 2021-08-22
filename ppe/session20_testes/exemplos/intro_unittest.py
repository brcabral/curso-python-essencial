"""
Introcução ao módulo Unittest

Unittest
 -> Testes unitários

O que são testes unitários?
 - É a forma de testar unidades individuais do código fonte
 - Unidades individuais podem ser: funções, métodos, classes, módulos, etc

Para criar os testes unitários em Python, é preciso criar classes que herdam de unittest.TestCase
e a partir de então ganhamos todos os 'assertions' presentes no módulo.

Para executar os testes, utilizamos unittest.main()

TestCase
 -> Casos de teste para sua unidade

Opções de assertion do unittest
 - https://docs.python.org/3/library/unittest.html#unittest.TestCase

Por convenção, todos os testes em um test case, deve ter seu nome iniciado com test_

# Para executar os testes com unittest:
 - Modo simples:
   -> python nome_do_modulo.py
 - Modo verbose (com detalhes)
   -> python nome_do_modulo.py -v

# Docstrings nos testes
 - Podemos acrescentar (e é recomendado) docstrings nos nossos testes
"""

# Prática - Utilizando a abordagem TDD

# Arquivos da aula: atividades.py e testes.py
