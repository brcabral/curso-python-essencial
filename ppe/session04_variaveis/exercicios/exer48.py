"""
Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
"""

seg_total = int(input('Digite o tempo total em segundos: '))
horas = int(seg_total / 3600)
minutos = int((seg_total % 3600) / 60)
segundos = int((seg_total % 3600) % 60)

print(f'O segundo digitado convertido em horas é: {horas}:{minutos}:{segundos}')
