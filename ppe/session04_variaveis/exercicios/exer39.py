"""
A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso.
Sendo que da quantida total:
 - o primeiro ganhador receberá 46%
 - o segundo receberá 32%
 - o terceiro receberá o restante
Calcule e imprima a quantidade ganha por cada um dos ganhadores.
"""

premio = 780_000.00
ganhador1 = premio - (premio * (1 - 0.46))
ganhador2 = premio - (premio * (1 - 0.32))
ganhador3 = premio - (ganhador1 + ganhador2)

print(f'O primeiro ganhador recebeu R$ {ganhador1}')
print(f'O segundo ganhador recebeu R$ {ganhador2}')
print(f'O terceiro ganhador recebeu R$ {ganhador3}')
