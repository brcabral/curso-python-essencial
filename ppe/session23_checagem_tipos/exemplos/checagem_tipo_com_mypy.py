"""
mypy
 - Ferramenta para verificar os tipos de dados do Python
 - instalar: pip install mypy
 - executar: mypy <nome_do_modulo>.py

O uso do mypy só tem sentido caso seja declarado o tipo das variáveis (type hinting)
"""


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f'{texto.title()}\n{"*" * len(texto)}'
    else:
        return f' {texto.title()} '.center(50, '#')


print(cabecalho('geek university'))
print(cabecalho('geek university', alinhamento=False))
print(cabecalho('geek university', alinhamento=True))
