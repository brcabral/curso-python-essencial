"""
Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite
o número de dias trabalhados pele encanador e imprima a quantia líquida que deverá
ser paga, sabendo-se que são descontados 8% para imposto de renda.
"""

dias_trabalhado = float(input('Quantos dias o encanador trabalhou? '))
vlr_liquido = (30 * dias_trabalhado) * 0.92
print(f'O valor líquido a ser pago é R$ {vlr_liquido} ')
