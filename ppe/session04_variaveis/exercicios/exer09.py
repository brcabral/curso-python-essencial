"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.
A formula de conversão é K = C + 273.15, sendo F a temperatura em Kelvin
e C a temperatura em Celsius
"""

temp_celsius = float(input("Digite a temperatura em Celsius: "))
temp_kelvin = temp_celsius + 273.15
print(f'A temperatura em Kelvin é {temp_kelvin}')
