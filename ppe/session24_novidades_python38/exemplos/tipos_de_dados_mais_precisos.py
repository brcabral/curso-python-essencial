"""
Tipo de dados mais precisos

Novos tipos de dados
 - Literal type
 - Union
 - Final
 - Typed dictionaries
 - Protocols
"""

# Literal type
"""
O literal type indica quais os possíveis retornos de uma função.
O retorno não é obrigatório e sim os esperados
"""

from typing import Literal


def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    return 'conectado'


print(pegar_status('Joao'))

print("--------------------------------------------------")


def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        # o !r coloca o valor em destaque entre aspas
        raise ValueError(f'Operação inválida {operacao!r}')


def calcula_v2(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        # o !r coloca o valor em destaque entre aspas
        raise ValueError(f'Operação inválida {operacao!r}')


calcula_v1('+', 6, 4)
calcula_v1('-', 10, 2)
# calcula_v1('*', 3, 5)

calcula_v2('+', 6, 4)
calcula_v2('-', 10, 2)
# calcula_v2('*', 3, 5)

print("--------------------------------------------------")

from typing import Union

# Union
"""
Indica que uma função pode retornar tipos diferentes de dados.
Pode indicar também que um parâmetro aceita tipos diferentes de dados.
"""


def soma(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1 + num2

    if resultado > 50:
        return f'O valor {resultado} é muito grande.'
    else:
        return resultado


print("--------------------------------------------------")

from typing import Final

# Final
"""
Usado para indicar constantes.
Lembrando que Python não é tipado, portanto o uso do final é apenas uma indicação e não uma obrigatoriedade
"""

NOME: Final = 'Geek'
print(NOME)

# Decorador final
"""
Indica que a classe e os métodos marcados como final não podem ser herdado ou sobrescrito, respectivamente.
"""

from typing import final


@final
class Pessoa:
    pass


class Estudante(Pessoa):
    pass

    @final
    def estudar(self):
        print('Estou estudando...')


class Estagiario(Estudante):
    pass

    def estudar(self):
        print('Estudando e estagiando')


print("--------------------------------------------------")

from typing import TypedDict

# Typed dictionaries
"""
Criar um dicionário tipado conforme tipos indicado nos atributos da classe.
"""


class CursoPython(TypedDict):
    versao: str
    atualizacao: int


geek = CursoPython(versao='3.8.5', atualizacao=2020)
print(geek)

print("--------------------------------------------------")

from typing import Protocol

# Protocol
"""
 Em Python o importante não é o tipo da classe e sim seus métodos e atributos.
 Portanto o importante para executar a função é que ela tenha o atributo titulo
e não que ela seja do tipo Curso 
"""


class Curso(Protocol):
    titulo: str


def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')


class Venda:
    titulo = 'oi'


v1 = Venda()
estudar(v1)
