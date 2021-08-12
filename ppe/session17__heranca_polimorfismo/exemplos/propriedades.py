"""
Propriedades
 -> O properties são decorators usados em métodos os quais usamos para acessar os atributos
privados de uma classe.
 -> Nem todos os atributos privados precisam ser expostos, somente aqueles que forem necessários
para atender as regras de negócio.

OBS.: Também é possível usar property em métodos 'comuns'
"""

"""
class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


conta1 = Conta('Ana Maria Ribeiro', 3000, 5000)
conta2 = Conta('Nelson Pereira', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

saldo_total = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma do saldo das contas é {saldo_total}')

print(conta1.__dict__)
conta1.set_limite(7000)
print(conta1.__dict__)
"""


# Refatorando a classe Conta usando o decorator property
class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, novo_titular):
        self.__titular = novo_titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite


conta1 = Conta('Ana Maria Ribeiro', 3000, 5000)
conta2 = Conta('Nelson Pereira', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

saldo_total = conta1.saldo + conta2.saldo
print(f'A soma do saldo das contas é {saldo_total}')

print(conta1.__dict__)
conta1.limite = 7000
print(conta1.__dict__)

print(f'O valor total da conta1 (saldo + limite) é {conta1.valor_total}')
print(f'O valor total da conta2 (saldo + limite) é {conta2.valor_total}')
