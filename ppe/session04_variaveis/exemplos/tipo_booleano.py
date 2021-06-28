"""
Tipo booleano

Obs.: Sempre com a inicial maiúscula

Errado: true, false
Certo: True, False
"""

ativo = False
print(f'Variável ativo = {ativo}')

# Negação (not)
"""
Fazendo uma negação, se o valor booleano for verdadeiro o resultado será falso e
se for falso o resultado será verdadeiro.
"""
print(f'Variável (not ativo) = {not ativo}')

# Ou (or)
"""
É uma operação binária, ou seja, depende de dois valores. Onde um ou outro deve ser verdadeiro
"""
print(f'True or True = {True or True}')
print(f'True or False = {True or False}')
print(f'False or True = {False or True}')
print(f'False or False = {False or False}')

# E (and)
"""
É uma operação binária, ou seja, depende de dois valores. Onde ambos devem ser verdadeiro
"""
print(f'True and True = {True and True}')
print(f'True and False = {True and False}')
print(f'False and True = {False and True}')
print(f'False and False = {False and False}')


print(f'5 > 6 = {5 > 6}')
print(f'5 < 6 = {5 < 6}')
print(f'6 == 6 = {6 == 6}')
print(f'4 <= 5 = {4 <= 5}')
print(f'7 >= 8 = {7 >= 8}')
print(f'7 < 8 or 4 > 6 = {7 < 8 or 4 > 6}')
print(f'7 < 8 and 4 > 6 = {7 < 8 and 4 > 6}')
