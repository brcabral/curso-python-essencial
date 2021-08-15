"""
MRO (Method Resolution Order - Resolução de Ordem de Métodos)
 -> É a ordem de execução dos métodos (quem será executado primeiro)
"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self.nome} está nadando'

    def cumprimentar(self):
        return f'Eu sou {self.nome} do mar!'


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self.nome} está andando'

    def cumprimentar(self):
        return f'Eu sou {self.nome} do terra!'


class Pinguim(Aquatico, Terrestre):
    def __init__(self, nome):
        super().__init__(nome)


tux = Pinguim('Tux')
print(tux.cumprimentar())

"""
Resultado da execução de: print(tux.cumprimentar())

class Pinguim(Aquatico, Terrestre):
  -> Eu sou Tux do mar!

class Pinguim(Terrestre, Aquatico):
  -> Eu sou Tux do terra!
"""

print("--------------------------------------------------")

# É possível conferir a ordem de execução dos métodos de 3 formas (exibe a ordem de onde vai produrar os métodos)
# Via propriedade __mro__
print(f'Propriedade: {Pinguim.__mro__}')

# Via método mro()
print(f'Método: {Pinguim.mro()}')

# Via help
print(f'Help: {help(Pinguim)}')
