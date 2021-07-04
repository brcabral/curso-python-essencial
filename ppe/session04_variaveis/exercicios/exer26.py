"""
Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares.
A fórmula de conversão é: H = M * 0,0001, sendo M a área em metros quadrados
e H a área em hectares
"""

met_quadrado = float(input('Digite a área em metros quadrados: '))
hectare = met_quadrado * 0.0001
print(f'A área em hectares é: {hectare}')
