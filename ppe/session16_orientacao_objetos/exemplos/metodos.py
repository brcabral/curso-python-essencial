"""
Métodos
 -> Representa os comportamentos do objeto, ou seja, as ações que este objeto pode realizar
no seu sistema

 -> Os métodos são escritos em letra minúscula, se o nome for composto o nome terá as palavras
separadas por underline.

Em Python, dividimos os métodos em 3 grupos:
  - Métodos de instância;
  - Métodos de classe;
  - Método estático

O método __init__ é um método especial chamado de construtor e sua função é construir
  um objeto da classe.

OBS.: Os métodos/funções dunder são chamados de métodos mágicos
 -> ATENÇÂO: Não é recomendado criar funções próprias utilizando dunder.
"""

# Biblioteca externa para usar criptografia em python
from passlib.hash import pbkdf2_sha256 as cryp


# Métodos de instâncias

class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.ligada = False


class ContaCorrente:
    contador = 999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limnite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:
    contador = 0

    def __init__(self, nome, sobrenome, email, senha):
        self.id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.id

    @classmethod
    def conta_usuarios(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) cadastrado(s).')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def get_senha(self):
        return self.__senha

    def check_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


p1 = Produto('PlayStation 4', 'Vídeo Game', 2300)
print(f'Valor do produto p1 com 10% de desconto: {p1.desconto(10)}')
print(f'Valor do produto p1 com 20% de desconto: {p1.desconto(20)}')

# Alternativa para chamar um método de instância (Classe.metodo(instância da classe, parametro)
print(f'Valor do produto p1 com 40% de desconto: {Produto.desconto(p1, 40)}')

print("--------------------------------------------------")

user1 = Usuario('Antonio', 'Pereira', 'antpereira@email.com.br', '123456')
user2 = Usuario('Laura', 'Malheiro', 'lauramalheiro@email.com.br', '654321')

print(f'Nome completo do usuário 1: {user1.nome_completo()}')
print(f'Nome completo do usuário 2: {user2.nome_completo()}')

print()
print(f'A senha do usuário 1 está correta? {user1.check_senha("123456")}')
print(f'A senha do usuário 1 está correta? {user1.check_senha("159753")}')

print()
print(f'Senha criptografada do usuário 1: {user1.get_senha()}')

print("--------------------------------------------------")

# Métodos de classes
"""
Métodos de classe em Python são conhecidos como métodos estáticos em outras linguagens
"""

user3 = Usuario('Antonio', 'Pereira', 'antpereira@email.com.br', '123456')
user4 = Usuario('Laura', 'Malheiro', 'lauramalheiro@email.com.br', '654321')

Usuario.conta_usuarios()

print("--------------------------------------------------")

# Método estático


class OutroUsuario:
    contador = 0

    def __init__(self, nome, sobrenome, email, senha):
        self.id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.id

    @classmethod
    def conta_usuarios(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) cadastrado(s).')

    @staticmethod
    def definicao():
        return 'Teste de método estático'


print(f'Acessando método estático: {OutroUsuario.definicao()}')

print("--------------------------------------------------")

# Métodos privados
"""
Por convenção criamos métodos privados iniciando eles com duplo underline.
"""


class NovoUsuario:
    contador = 0

    def __init__(self, nome, sobrenome, email, senha):
        self.id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.id
        print(f'Usuário {self.__gera_usuario()} criado com sucesso!')

    @classmethod
    def conta_usuarios(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) cadastrado(s).')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def get_senha(self):
        return self.__senha

    def check_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


user5 = NovoUsuario('Carla', 'Alves', 'carla@email.com.br', '123456')
