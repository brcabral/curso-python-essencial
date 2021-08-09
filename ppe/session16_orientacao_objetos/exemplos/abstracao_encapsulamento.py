"""
Abstração e encapsulamento

O grande objetivo ad POO é encapsular nosso código dentro de um grupo lógico
  e hierarquico utilizando classes.

Abstração
 -> Em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos
e métodos privados do usuário

"""


class Conta1:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta1.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta1.contador += 1

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


conta1 = Conta1('Geek', 150.00, 1500)
print(f'Número da conta: {conta1.numero}')
print(f'Titular da conta: {conta1.titular}')
print(f'Saldo da conta: {conta1.saldo}')
print(f'Limite da conta: {conta1.limite}')
conta1.extrato()

print("--------------------------------------------------")

# Protegendo os atributos, alterando o acesso deles para privados


class Conta2:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta2.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta2.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo.')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor deve ser positivo')

    def transferir(self, valor, conta_destino):
        # 1. remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10  # taxa de transferência

        # 2. Adicionar o valor na conta de destino
        conta_destino.__saldo += valor


conta2 = Conta2('Geek', 150.00, 1500)
print(conta2.__dict__)

print('Depositando R$ 150...')
conta2.depositar(150)
print(conta2.__dict__)

print('Sacando R$ 200...')
conta2.sacar(200)
print(conta2.__dict__)

print("--------------------------------------------------")

conta3 = Conta2('Angelina', 150.00, 1500)
conta3.extrato()

conta4 = Conta2('Felicity', 300.00, 2000)
conta4.extrato()

print('Transferindo R$ 100 da conta4 para conta3')
conta4.transferir(100, conta3)
conta3.extrato()
conta4.extrato()
