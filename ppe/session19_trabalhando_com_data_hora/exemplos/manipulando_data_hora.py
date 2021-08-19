"""
Manipulando data e hora
 - Python tem um módulo built-in para trabalhar com data e hora chamado datetime
"""

import datetime

# print(dir(datetime))

# Ano mínimo e ano máximo suportado pelo Python
print(f'MINYEAR: {datetime.MINYEAR}')
print(f'MAXYEAR: {datetime.MAXYEAR}')

print("--------------------------------------------------")

# Retorna a data e hora atual
print(f'Data/hora atual: {datetime.datetime.now()}')
print(f'repr da data/hora atual: {repr(datetime.datetime.now())}')

print("--------------------------------------------------")

# Com o replace() é possível alterar a data e hora
inicio = datetime.datetime.now()
print(f'inicio: {inicio}')

# Alterar o horário para 16 horas, 0 minuto, 0 segundos e 0 milésimo
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

print(f'inicio com hora alterada: {inicio}')

print("--------------------------------------------------")

# Criar uma data
evento = datetime.datetime(2021, 8, 16, 8)
print(f'data/hora evento: {evento}')

print("--------------------------------------------------")

# Convertendo data/hora string em datetime
nascimento = '04/06/1985'
nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(f'nascimento: {nascimento}')

print("--------------------------------------------------")

# Acessando os elementos de data e hora
data_hora_atual = datetime.datetime.now()

print(f'Ano: {data_hora_atual.year}')  # ano
print(f'Mês: {data_hora_atual.month}')  # mês
print(f'Dia: {data_hora_atual.day}')  # dia
print(f'Hora: {data_hora_atual.hour}')  # hora
print(f'Minuto: {data_hora_atual.minute}')  # minuto
print(f'Segundo: {data_hora_atual.second}')  # segundo
print(f'Milissegundo: {data_hora_atual.microsecond}')  # milissegundo
