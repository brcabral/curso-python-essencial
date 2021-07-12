"""
Receba a altura do degrau de uma descada e a altura que o usuário deseja alcançar
subindo a escada. Calcule e moster quantos degraus o usuário deverá subir para
atingir seu objetivo
"""

degrau_atual = int(input('Qual o degrau você está? '))
degrau_destino = int(input('Qual o degrau você deseja chegar? '))
print(f'Você deve subrir {degrau_destino - degrau_atual} degrau(s) para chegar no degrau desejado.')
