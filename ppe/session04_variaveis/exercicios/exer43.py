"""
Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
 - o total a pagar com desconto de 10%
 - o valor de cada parcela, no parcelamento de 3x sem juros
 - a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
 - a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
"""
from builtins import input, print

valor = float(input('Digite o valor total da compra R$ '))
print(f'O valor total com desconto (10%): R$ {valor * 0.9}')
print(f'O valor total de cada parcela (3x): R$ {valor / 3}')
print(f'A comissão do vendedor em caso de venda a vista: R$ {valor * 0.9 * 0.05}')
print(f'A comissão do vendedor em caso de venda a prazo: R$ {valor * 0.05}')
