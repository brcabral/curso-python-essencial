"""
Atributos
  -> Representam as características do objeto, ou seja, pelos atributos nós conseguimos
representar computacionamente os estados de um objeto

Em Python, dividimos os atributos em 3 grupos:
  - Atributos de instância;
  - Atributos de classe;
  - Atributos dinâmicos;

Em Python, por convenção, ficou estabelecido que todos os atributos de uma classe são públicos.
Para declarar que um atributo é privado, devemos usar __ (duplo underscore) no início de seu nome.
  -> Isso também é conhecido como Name Mangling
"""

# Atributos de instâncias
"""
  - São atributos declarados dentro do método construtor
  - Todos os atributos abaixo são públicos.
  - Ao criar uma instâncias/objetos de uma classe, todas as instâncias terão estes atributos.
"""


class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limnite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Classes com atributos privados
# OBS.: O conceito de atributo privado em Python, é apenas uma convenção, a linguagem não vai
# impedir que façamos acesso aos atributos sinalizados como privados fora da classe

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha


# Exemplo
user = Acesso('user@email.com', '123456')
print(f'Email: {user.email}')

# print(f'Senha: {user.__senha}')  # AttributeError

# Temos acesso, mas não devemos acessr o atributo. (user._Acesso__senha -> Name mangling)
print(f'Senha: {user._Acesso__senha}')

print("--------------------------------------------------")

# Atributos de classe
"""
 - São declarados diretamente na classe, fora do construtor.
Geralmente já iniciamos um valor, e este valor é compartilhado entre todas as intâncias da classe.
Ou seja, todas as intâncias terão o mesmo valor para este atributo.

 - Não preisamos criar uma instância de uma classe para acessar um atributo de classe.
 
OBS.: atributo "static" em Java
"""


class Produto2:
    # Atributo de classe
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto2.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto2.imposto
        Produto2.contador = self.id


p1 = Produto2('PlayStation 4', 'Vídeo Game', 2300)
p2 = Produto2('Xbox S', 'Vídeo Game', 4500)

print(f'ID p1: {p1.id}')
print(f'Nome p1: {p1.nome}')
print(f'Valor p1: {p1.valor}')
# Forma incorreta de acessar um atributo de classe
print(f'Imposto do p1: {p1.imposto}')

print()

print(f'ID p2: {p2.id}')
print(f'Nome p2: {p2.nome}')
print(f'Valor p2: {p2.valor}')
# Forma incorreta de acessar um atributo de classe
print(f'Imposto do p2: {p2.imposto}')

print()

# Acessar o valor sem precisar instânciar a classe
# Forma correta de acessar um atributo de classe
print(f'Imposto da classe produto: {Produto2.imposto}')

print("--------------------------------------------------")

# Atributos dinâmicos
"""
Um atributo de instância que pode ser criado em tempo de execução.

OBS.: O atributo dinâmico será exclusivo da instância que o criou.
"""

p3 = Produto2('PlayStation 4', 'Vídeo Game', 2300)
p4 = Produto2('Arroz', 'Mercearia', 25.99)

# Criando um atributo dinâmico em tempo de execução
p4.peso = '5kg'  # note que na classe Produto não existe o atributo peso
print(f'Produto: {p4.nome}, descrição: {p4.descricao}, valor: {p4.valor}, peso: {p4.peso}')

# Exibindo os dados de uma instância (retorna um dicionário)
print()
print(p3.__dict__)
print(p4.__dict__)

# Deletando um atributo
print()
del p4.peso
del p4.descricao
print('>>> Após retirar o atributo descricao e peso de p4')
print(p4.__dict__)
