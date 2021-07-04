"""
Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
A fórmula de conversão é: C = P * 2,54, sendo C o comprimento em centímetros e
P o comprimento em polegadas
"""

polegada = float(input('Digite o comprimento em polegada: '))
centimetro = polegada * 2.54
print(f'O comprimento em centímetro é: {centimetro}')
