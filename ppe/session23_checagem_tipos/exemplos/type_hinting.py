"""
Type hinting
 - Com o type hinting você especifica o tipo de dados que deve ser usado.

Recurso implementado na versão 3.5
"""


def cumprimentar(nome: str) -> str:
    return f'Olá, {nome}'


print(cumprimentar('Geek'))

# Usar o type hinting não impede do programa executar com passagem de dados de tipo inválido
# porém a IDEs ou ferramentas de checagem de tipo irá informar que o tipo está incorreto
print(cumprimentar(1))

print("--------------------------------------------------")


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f'{texto.title()}\n{"*" * len(texto)}'
    else:
        return f' {texto.title()} '.center(50, '#')


print(cabecalho('geek university'))
print(cabecalho('geek university', alinhamento=False))
