"""
Leia uma velocidade em km/h (quilômetro por hora) e apresente-a convertida em m/s
(metros por segundo). A fórula de conversão é: M = K / 3.6, sendo K a velocidade
em km/h e M em m/s.
"""

vel_km = float(input('Digite a velocidade em km/h: '))
vel_m = vel_km / 3.6
print(f'A velocidade em m/s: {vel_m}')
