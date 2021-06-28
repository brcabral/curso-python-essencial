"""
Tipo float (casas decimais)

Obs: O separador de casas decimais é o ponto e não a vírgula
"""
# Errado considerando gerar um float
# valor = 1,44

#Certo
valor = 1.44
print(f'Variável valor = {valor}')
print(f'Tipo da variável valor = {type(valor)}')

# É possível fazer dupla atrituição (usando virgula)
valor1, valor2 = 1, 44
print(f'Variável valor1 = {valor1}')
print(f'Variável valor2 = {valor2}')

# Converter um float para int
result = int(valor)
print(f'Variável result (int(valor)) = {result}')

# Converter um int em um fload
num_int = 10
num_cast = float(num_int)
print(f'Variável num_cast = {num_cast}')
print(f'Tipo da variável num_cast = {type(num_cast)}')

# É possíevel trabalhar com números complexos
num_complexo = 5j
print(f'Variável num_complexo = {num_complexo}')
print(f'Tipo da variável num_complexo = {type(num_complexo)}')
print(f'num_complexo ** 2 = {num_complexo ** 2}')
