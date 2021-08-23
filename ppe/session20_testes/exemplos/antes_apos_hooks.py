"""
Unittest - Antes e após hooks

Hooks
 - São os testes em si, ou seja, a execução dos testes

setUp()
 -> É executado antes de cada método de teste. É util para criarmos instâncias de objetos e outros dados;

tearDown()
 -> É executado ao final de cada método de teste. É útil para excluir dados ou fechar conexões com o BD
"""

import unittest


class ModuloTest(unittest.TestCase):
    def setUp(self):
        # Configurações do setUp()
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # teste ...
        # tearDown() vai rodar após o teste
        pass

    def test_segundo(self):
        # setUp vai rodar antes do teste
        # teste ...
        # tearDown() vai rodar após o teste
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass


print("--------------------------------------------------")

# Arquivos da aula: robo.py e robo_testes.py
