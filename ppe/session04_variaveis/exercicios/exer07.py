"""
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A formula de conversão é C = 5.0 * (F - 32.0) / 9.0, sendo C a temperatura em Celsius
e F a temperatura em Fahrenheit
"""

temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
temp_celsius = 5.0 * (temp_fahrenheit - 32.0) / 9.0
print(f'A temperatura em Fahrenheit é {temp_celsius}')
