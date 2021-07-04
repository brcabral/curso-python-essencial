"""
Leia uma distância em quilômetros e apresente-a convertida em milhas.
A fóruma de conversão é M = K / 1,61, sendo K a distância em quilômetro
e M e milhas
"""

km = float(input('Digite a distância em quilômetro: '))
milha = km / 1.61
print(f'A distância em milhas é: {milha}')
