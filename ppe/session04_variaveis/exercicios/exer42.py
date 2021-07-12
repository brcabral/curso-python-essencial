"""
Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sanbendo-se
que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga
7% de imposto sobre o salário-base.
"""

salario_base = float(input('Digite o salário-base do funcionário: '))
salario_receber = salario_base * 1.05 * 0.93
print(f'O salário a receber é R$ {salario_receber}')
