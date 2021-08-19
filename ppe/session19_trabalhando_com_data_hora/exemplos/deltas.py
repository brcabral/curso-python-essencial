"""
Trabalhando com deltas de data e hora
 - Delta de data e hora é a diferença entre duas datas
"""

import datetime

# Calcular tempo para um determinado evento
data_atual = datetime.datetime.now()
centenario_afe = datetime.datetime(2050, 4, 12)

tempo_para_centenario = centenario_afe - data_atual
print(tempo_para_centenario)
print(f'Faltam {tempo_para_centenario.days} dias, {tempo_para_centenario.seconds // 60 // 60} '
      f'horas para o centenário da Ferroviária!!')

print()
print(f'Tipo da variável centenario_afe: {type(centenario_afe)}')
print(f'Tipo da variável tempo_para_centenario: {type(tempo_para_centenario)}')

print("--------------------------------------------------")

data_da_compra = datetime.datetime.now()
print(f'Data da compra: {data_da_compra}')

regra_boleto = datetime.timedelta(days=3)
print(f'regra do boleto: {regra_boleto}')

vencimento_boleto = data_da_compra + regra_boleto
print(f'Vencimento do boleto: {vencimento_boleto}')
