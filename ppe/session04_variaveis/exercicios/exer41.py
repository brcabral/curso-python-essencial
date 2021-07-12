"""
Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas
trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre
o valor calculado
"""

vlr_hora = float(input('Digite o valor da hora de trabalho (em reais): '))
hora_trabalhada = float(input('Digite a quantidade de horas trabalhadas: '))
vlr_pago = (vlr_hora * hora_trabalhada) * 1.1
print(f'O valor a ser pago ao funcionário é R$ {vlr_pago}')
