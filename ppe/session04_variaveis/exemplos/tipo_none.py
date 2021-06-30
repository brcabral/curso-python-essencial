"""
Tipo None

O tipo de dado None em Python representa que uma variável não tem tipo,
pode ser dito que é do tipo vazio, porém o mais correto é dizer que é sem tipo

OBS.: O tipo None é SEMPRE especificado com a primeira letra maiúscula
 - (Certo: None | Errado: none)

Quando utilizamos?
 - Podemos utilizar None quando queremos criar uma variável e iniciá-la sem um tipo,
 antes de recebermos um valor final.

OBS.: O tipo None é sempre considerado como false
"""

numeros = None
print(f'numeros: {numeros}')
print(f'Tipo da variável numeros = {type(numeros)}')

if numeros:
    print('Não à elementos na variável')
else:
    print('Há elementos na variável')

numeros = 1.44, 1.34, 5.67
print(f'numeros: {numeros}')
print(f'Tipo da variável numeros = {type(numeros)}')
