"""
Polimorfismo
 -> Um objeto pode ter várias formas
"""
from abc import ABC


class Animal(object):
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.nome} fala wau wau')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.nome} fala miau')


class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.nome} fala algo...')


# Testes
felix = Gato('Felix')
felix.comer()
felix.falar()

print()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

print()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()
