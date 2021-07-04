"""
Leia uma velocidade em m/h (metro por segundo) e apresente-a convertida em km/h
(quilômetro por hora). A fórula de conversão é: K = M * 3.6, sendo K a velocidade
em km/h e M em m/s.
"""
from builtins import int

vel_ms = float(input('Digite a velocidade em m/s: '))
vel_km = vel_ms * 3.6
print(f'A velocidade em m/s: {vel_km}')
