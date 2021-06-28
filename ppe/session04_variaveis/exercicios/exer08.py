"""
Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
A formula de conversão é C = K - 273.15, sendo C a temperatura em Celsius
e C a temperatura em Kelvin
"""

temp_kelvin = float(input("Digite a temperatura em Kelvin: "))
temp_celsius = temp_kelvin - 273.15
print(f'A temperatura em Kelvin é {temp_celsius}')
