"""
Reversed
 - Inverte o iterável
 - A função retorna uma iterável chamado list reverse iterator, mas podemos converter o elemento
retornado em uma lista, tupla ou conjunto

OBS.: Não confunda reversed() com a função reverse(). O reverse() só funciona em listas.
O reverse() pode ser usado apenas em listas, já o reversed() podemos usar em qualquer iterável
"""

numeros = [1, 2, 3, 4, 5]
numeros_reversed = reversed(numeros)
print(f'Lista numeros: {numeros_reversed}')
print(f'Lista numeros_reversed: {numeros_reversed}')
print(f'Tipo da variável lista_reversed: {type(numeros_reversed)}')

# Conbertendo o elemento retornado em uma lista, tupla ou conjunto
# Lista
print(f'A variável numeros invertida formato lista: {list(reversed(numeros))}')

# Tupla
print(f'A variável numeros invertida formato tupla: {tuple(reversed(numeros))}')

# Conjunto (set)
#  Conjunto não guarda ordem de entrada, por isso não é garantia do retorno ordenado
print(f'A variável numeros invertida formato conjunto: {set(reversed(numeros))}')

print("--------------------------------------------------")

# Iterando sobre o reversed
for num in reversed(range(0, 11)):
    print(f'{num} ', end='')

print()

for letra in reversed('Geek University'):
    print(f'{letra} ', end='')

print()
# Obtendo o mesmo resultado do exemplo anterior sem o for
print(' '.join(list(reversed('Geek University'))))

# Porém a forma mais fácil para obter esse resultado é usando o slice de string
# Mas não é possível configurar sua saída
print('Geek University'[::-1])
