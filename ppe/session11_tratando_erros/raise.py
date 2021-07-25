"""
Levantando (lançando) os próprios erros com raise
O raise não é uma função. É uma palavra reservada

raise -> lança exeções
  - O raise é usado para criarmos nossas próprias exeções e mensagens de erro.

Forma de uso
  - raise TipoDoErro('Mensagem de erro')

OBS.: O raise finaliza a função. Nenhum código após o raise será executado
"""


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek', 'azul')
# colore('Geek', 4)
# colore(True, 'azul')
# colore('Geek University', 'verde')
# colore('Geek University', 'preto')

print("--------------------------------------------------")
