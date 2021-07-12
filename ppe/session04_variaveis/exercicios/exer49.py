"""
Faça um programa que leia o horário (hora, minuto e segundo) de início e a duração,
em segundos, de uma experiência biológica. O programa deve resultar com o novo horário
(hora, minuto e segundo) do termino da mesma.
"""

hora = int(input('Digite a hora de início da experiência: '))
minuto = int(input('Digite o(s) minuto(s) de início da experiência: '))
segundo = int(input('Digite o(s) segundo(s) de início da experiência: '))
duracao = int(input('Digite a duração da experiência (em segundos): '))

segundos_inicial = (hora * 3600) + (minuto * 60) + segundo
segundos_final = segundos_inicial + duracao

horas = int(segundos_final / 3600)
minutos = int((segundos_final % 3600) / 60)
segundos = int((segundos_final % 3600) % 60)

print(f'O horario final da experiência foi: {horas}:{minutos}:{segundos}')
