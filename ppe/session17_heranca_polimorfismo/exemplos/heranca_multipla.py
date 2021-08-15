"""
Herança múltipla
 -> É possível que uma classe herde várias classes, fazendo com que a classe filha
herde todos os atributos e métodos das classes herdadas.

OBS.: A herança múltipla pode ser feita de duas maneiras:
 - Por multiderivação direta;
 - Por multiderivação indireta;
"""


# Excemplo 1 - Multiderivação direta
class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivadaDireta(Base1, Base2, Base3):
    pass


# Excemplo 2 - Multiderivação indireta
class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerivadaIndireta(Base3):
    pass


print("--------------------------------------------------")


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


baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

print()

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

print()

tux = Pinguim('Tux')
print(tux.nadar())
print(tux.andar())
print(tux.cumprimentar())  # ??? -> Method Resolution Order (MRO)

print("--------------------------------------------------")

print(f'Tux é instância de Pinguim? {isinstance(tux, Pinguim)}')
print(f'Tux é instância de Aquatico? {isinstance(tux, Aquatico)}')
print(f'Tux é instância de Terrestre? {isinstance(tux, Terrestre)}')
print(f'Tux é instância de Animal? {isinstance(tux, Animal)}')
print(f'Tux é instância de object? {isinstance(tux, object)}')
