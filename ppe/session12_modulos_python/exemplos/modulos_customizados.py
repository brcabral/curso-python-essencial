"""
Módulos Customizados
"""
from meus_modulos import soma_impares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Somando a lista numeros: {soma_impares(numeros)}')

print("--------------------------------------------------")

import meus_modulos as mm
print(mm.lista)
print(mm.soma_impares(mm.lista))

print("--------------------------------------------------")

# from session10_lambdas_func_integradas.exemplos.map import cidades, c_para_f
from meus_modulos import cidades, c_para_f
print(list(map(c_para_f, cidades)))
