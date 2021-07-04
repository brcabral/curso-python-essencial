"""
Leia uma distância em milhas e apresente-a convertida em quilômetros.
A fóruma de conversão é K = 1,61 * M, sendo K a distância em quilômetro
e M e milhas
"""

milhas = float(input('Digite a distância em milhas: '))
km = 1.61 * milhas
print(f'A distância em quilômetro é: {km}')
