"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A formula de conversão é F = C * (9.0 / 5.0) + 32.0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius
"""

temp_celsius = float(input("Digite a temperatura em Celsius: "))
temp_fahrenheit = temp_celsius * (9.0 / 5.0) + 32.0
print(f'A temperatura em Fahrenheit é {temp_fahrenheit}')
