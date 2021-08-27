"""
Annotations

# Correto (Variável ou parâmetro)
texto: str

# Incorreto (Variável ou parâmetro)
texto:str
texto : str

-----------------------------------

# Correto (tipo de retorno)
) -> str

# Incorreto (tipo de retorno)
)->str
)-> str
) ->str

-----------------------------------

# Quando for inicializar um valor
# Correto
alinhamento: bool = True

# Incorreto

alinhamento : bool = True
alinhamento:bool = True
alinhamento: bool= True
alinhamento: bool =True
alinhamento: bool=True

"""
import math


def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio


print(f'Annotations da função circunferencia: {circunferencia.__annotations__}')

print("--------------------------------------------------")

# Declarando variáveis

nome: str = 'Geek University'
peso: float = 67.9
ativo: bool = True

print(f'Variável nome: {nome}')
print(f'Variável peso: {peso}')
print(f'Variável ativo: {ativo}')

# print(nome.__annotations__)  # Não tem annotations
print(f'Annotations das variáveis globais: {__annotations__}')

print("--------------------------------------------------")


class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando...'


p = Pessoa(nome='Geek University', idade=37, peso=69.5)
print(p.__dict__)

# print(p.__annotations__)  # Classes não tem annotations
print()

print(f'Annotations da função andar da classe Pessoa: {p.andar.__annotations__}')
print(f'Annotations da função init da classe Pessoa: {p.__init__.__annotations__}')
