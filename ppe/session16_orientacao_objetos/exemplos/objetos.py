"""
Objetos
 -> São instâncias da classe. Podemos criar vários objetos a partir de uma classe.
Podemos pensar nos objetos como variáveis do tipo definido na classe.
"""


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class ContaCorrente:
    contador = 999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limnite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Usuario:
    contador = 0

    def __init__(self, nome, sobrenome, email, senha):
        self.id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
        Usuario.contador = self.id


# Instâncias/objetos
lamp1 = Lampada('branca', 110, 3500)
cc1 = ContaCorrente(5000, 20000)
user1 = Usuario('Daniela', 'Amorim', 'dani_amorim@email.com.br', '123456')

print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')
lamp1.ligar_desligar()
print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

input_nome = 'Priscila'
input_sobrenome = 'Miranda'
input_email = 'primir@email.com.br'
input_senha = '123456'

user2 = Usuario(input_nome, input_sobrenome, input_email, input_senha)
print()
print(f'Tipo da variável user2: {type(user2)}')
print(f'Usuário 2: {user2.__dict__}')

print("--------------------------------------------------")


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf


class CC:
    def __init__(self, cliente, email, senha):
        self.id = Usuario.contador + 1
        self.__cliente = cliente
        self.__email = email
        self.__senha = senha
        Usuario.contador = self.id

    def mostra_cliente(self):
        print(f'O cliente é : {self.__cliente._Cliente__nome}')


cli1 = Cliente('Marcos', 'Almeida', '123.456.789-00')
cc = CC(cli1, 'almeida.marcos@banco.com.br', '159753')

print(f'Dados da CC: {cc.__dict__}')
# print(f'Dados do cliente da CC: {cc.__cliente.__dict__}')
cc.mostra_cliente()
