"""
Métodos de data e hora
"""

import datetime

# A diferença entre now() e today(), é que com o now() podemos especificar o timezone
import timeit

agora = datetime.datetime.now()
print(f'variável agora: {agora}')
print(f'Tipo da variável agora: {type(agora)}')
print(f'Repr da variável agora: {repr(agora)}')

print()

today = datetime.datetime.now()
print(f'variável today: {today}')
print(f'Tipo da variável today: {type(today)}')
print(f'Repr da variável today: {repr(today)}')

print("--------------------------------------------------")

# Difinir meia-noite usando o combine()
manutencao = datetime.datetime.combine(datetime.datetime.now() + datetime.timedelta(days=1), datetime.time())
print(f'variável manutencao: {manutencao}')
print(f'Tipo da variável manutencao: {type(manutencao)}')
print(f'Repr da variável manutencao: {repr(manutencao)}')

print("--------------------------------------------------")

# Retornar o dia da semana, de uma data, com o método weekday().
# O método weekday retorna um int, sendo 0 (zero) a segunda-feira
"""
|-------------------------------|
| 0 | Monday    | Segunda-feira |
| 1 | Tuesday   | Terça-feira   |
| 2 | Wednesday | Quara-feira   |
| 3 | Thursday  | Quinta-feira  |
| 4 | Friday    | Sexta-feira   |
| 5 | Saturday  | Sábado        |
| 6 | Sunday    | Domingo       | 
|--------------------------------
"""

dia_semana = datetime.datetime.combine(datetime.datetime.now() + datetime.timedelta(days=1), datetime.time())
print(f'Dia da semana: {manutencao.weekday()}')

print("--------------------------------------------------")

nascimento = '04/06/1985'
nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

if nascimento.weekday() == 0:
    print('Você nasceu em uma segunda-feira')
elif nascimento.weekday() == 1:
    print('Você nasceu em uma terça-feira')
elif nascimento.weekday() == 2:
    print('Você nasceu em uma quarta-feira')
elif nascimento.weekday() == 3:
    print('Você nasceu em uma quinta-feira')
elif nascimento.weekday() == 4:
    print('Você nasceu em uma sexta-feira')
elif nascimento.weekday() == 5:
    print('Você nasceu em uma sábado')
elif nascimento.weekday() == 6:
    print('Você nasceu em uma domingo')

print("--------------------------------------------------")

# Formatando data/hora com strftime() - String Format Time
hoje = datetime.datetime.now()
print(f'variável hoje: {hoje}')

# y -> 21 | Y -> 2021
hoje_formatado = hoje.strftime('%d/%m/%Y %H:%M:%S')
print(f'Data formatada: {hoje_formatado}')

# b -> Aug | B -> August
mes = hoje.strftime('%B')
print(f'Mês: {mes}')

# Doc para configurar formatação da data/time
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

print("--------------------------------------------------")

from textblob import TextBlob


# O método translate utiliza a internet para fazer a tradução, por isso cuidado ao usar o método
def formata_data(data):
    return f'{data.day} de {TextBlob(data.strftime("%B")).translate(to="pt-br")} de {data.year}'


hoje = datetime.datetime.now()
print(f'variável hoje: {hoje}')
print(f'Data formatada: {formata_data(hoje)}')

print("--------------------------------------------------")

# Forma pythonica de converter uma string em datetime
dia = datetime.datetime.strptime('20/08/2021', '%d/%m/%Y')
print(f'variável dia: {dia}')
print(f'Tipo da variável dia: {type(dia)}')

print("--------------------------------------------------")

# Obter somente a hora
almoco = datetime.time(12, 30, 0)
print(f'variável almoco: {almoco}')

print("--------------------------------------------------")

# Marcando tempo de execução de uma operação com o timeit
import timeit

# Loop for
tempo_loop = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f'Tempo usando o loop for: {tempo_loop}')

# List Comprehension
tempo_list = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(f'Tempo usando o loop for: {tempo_list}')

# Map
tempo_map = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(f'Tempo usando o loop for: {tempo_map}')

print("--------------------------------------------------")

# Marcando o tempo de execução de uma função
import functools


def calculo(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


print(timeit.timeit(functools.partial(calculo, 2), number=10000))
