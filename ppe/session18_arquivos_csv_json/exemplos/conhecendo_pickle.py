"""
Conhecendo o Pickle
 -> O pickle é usado para serializar e desserializar um objeto.
   - Objeto Python -> Binário
   - Binário -> Objeto Python

OBS.: O módulo Pickle não é seguro contra dados maliciosos e desta forma não é recomendado
trabalhar com arquivos pickle vindos de outras pessoas que você não conhece ou de fontes
desconhecidas.
"""

import pickle


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendo..')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def miar(self):
        print(f'{self.nome} está comendo..')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def latir(self):
        print(f'{self.nome} está comendo..')


# Criar arquivo binário
felix = Gato('Gato')
pluto = Cachorro('Pluto')

# WB -> Indica que estamos trabalhando com o arquivo no modo escrita (w) e binário (b)
with open('arquivos/animais.pickle', 'wb') as arquivo:
    # dump(objeto | lista de objeto, arquivo)
    # pickle.dump(felix, arquivo)
    pickle.dump((felix, pluto), arquivo)

print("--------------------------------------------------")

# Ler arquivo binário

# RB -> Indica que estamos trabalhando com o arquivo no modo leitura (r) e binário (b)
with open('arquivos/animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato.nome}')
    gato.miar()
    print(f'Tipo da variável gato: {type(gato)}')

    print()

    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.latir()
    print(f'Tipo da variável cachorro: {type(cachorro)}')
