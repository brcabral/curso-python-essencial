"""
Herança (Inheritance)
 -> Reaproveitar código
 -> Extender nossas classes

OBS.: Com herença, a partir de uma classe existente, nós extendemos outra classe que passa
a herdar atributos e métodos da classe herdada

PERGUNTAR: Existe alguma entidade genérica o suficiente para encapsular os atributos
e métodos comuns a outras entidades?

A Classe herdade é conhecida por:
 - Super classe;
 - Classe mãe;
 - Classe pai;
 - Classe base;
 - Classe genérica

A Classe que herda é conhecida por:
 - Sub classe;
 - Classe filha;
 - Classe específica;

Sobrescrita de método
 - Ocorre quando reescrevemos/reimplementamos um método presente na super classe
em classes filhas
"""

"""
class Cliente:
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Julia', 'Andrade', '123.456.789-00', 5000)
funcionario1 = Funcionario('Carlos', 'Amazio', '987.654.321.11', 1234)

print(f'Cliente1: {cliente1.nome_completo()}')
print(f'Funcionario1: {funcionario1.nome_completo()}')
"""


# Refatorando as classes utilizando herança
class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa (logo, cliente é uma pessoa)"""
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma não comum de acessar dados da super classe
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionário herda de Pessoa (logo, funcionário é uma pessoa)"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma comum de acessar dados da super classe
        self.__matricula = matricula

    def nome_completo(self):
        print(f'Nome do funcionário: {super().nome_completo()}')
        return f'O funcionário {self._Pessoa__nome} {self._Pessoa__sobrenome} tem a matricula {self.__matricula}'


cliente1 = Cliente('Julia', 'Andrade', '123.456.789-00', 5000)
funcionario1 = Funcionario('Carlos', 'Amazio', '987.654.321.11', 1234)

print(f'Cliente1: {cliente1.nome_completo()}')
print(f'Funcionario1: {funcionario1.nome_completo()}')

print(cliente1.__dict__)
print(funcionario1.__dict__)

print("--------------------------------------------------")

# Sobrescrita de métodos (overriding)
# Sobrescrito o método nome_completo da classe funcionário
print(f'Cliente1: {cliente1.nome_completo()}')
print(f'Funcionario1: {funcionario1.nome_completo()}')
