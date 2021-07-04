"""
Leia um valor de área em metros quadrados m² e apresente-o convertido em acres.
A fórmula de conversão é: A = M * 0,000247, sendo M a área em metros quadrados
e A a área em acres
"""

met_quadrado = float(input('Digite a área em metros quadrados: '))
acre = met_quadrado * 0.000247
print(f'A área em acres é: {acre}')
