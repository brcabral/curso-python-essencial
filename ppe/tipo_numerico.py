"""
Tipo numérico
"""
num = 42
print(f'Variável num = {num}')
print(f'5 + 4 = {5 + 4}')
print(f'7 - 2 = {7 - 2}')
print(f'3 * 5 = {3 * 5}')
print(f'5 / 2 = {5 / 2}')

# Para retornar um inteiro da divisão
# Pode fazer um cast explicito
print(f'int(5 / 2) = {int(5 / 2)}')
# Ou usar duas barras
print(f'5 // 2 = {5 // 2}')

# Verificar o resto de uma divisão (modulo)
print(f'8 % 2 = {8 % 2}')
print(f'7 % 2 = {7 % 2}')

# Para calcular potência de um número
print(f'3 ** 3 = {3 ** 3}')
print(f'2 ** 8 = {2 ** 8}')

# Para facilitar a visualização, pode usar _ como separador
# O Python trata o número sem o _
print(1_000_000)

print(f'Variável num = {num}')
# Adicionar um valor de uma variável
num += 1
print(f'Variável num = {num}, após a adição (num += 1)')

# Subtrair um valor de uma variável
num -= 1
print(f'Variável num = {num}, após a subtração (num -= 1)')

# Multiplicar um valor de uma variável
num *= 2
print(f'Variável num = {num}, após a multiplicação (num *= 2)')

# Dividir um valor de uma variável
num /= 2
print(f'Variável num = {num}, após a divisão (num /= 2)')

# Dividir um valor de uma variável, arredondando o resultado
num //= 2
print(f'Variável num = {num}, após a divisão arredondando (num //= 2)')

# Verificar o tipo da variável
print(f'Tipo da variável num = {type(num)}')

x = 10
print(f'Tipo da variável x = {type(x)}')
