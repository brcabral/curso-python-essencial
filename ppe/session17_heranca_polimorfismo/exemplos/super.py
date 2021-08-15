"""
Métodos super()
 -> O método super() se refere a super classe.
"""


class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} faz {som}')


class Gato(Animal):
    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie)
        # super(Gato, self).__init__(nome, especie)
        super().__init__(nome, especie)
        self.__raca = raca


uni = Gato('Uni', 'Felina', 'SRD')
gracinha = Gato('Gracinha', 'Felina', 'SRD')
kinder = Gato('Kinder', 'Felina', 'SRD')

uni.faz_som('maiu maiu')
gracinha.faz_som('nhaiu')
kinder.faz_som('miauuu')
