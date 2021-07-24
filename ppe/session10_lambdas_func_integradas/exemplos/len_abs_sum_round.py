"""
Len, Abs, Sum, Round

# Len
  - len() -> Retorna o tamanho, quantidade de itens, de um iterável

# Abs
  - abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor sem o sinal

# Sum
  - sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial e retorna a soma total dos elementos,
incluíndo o valor inicial.
OBS.: O valor inicial default = 0

# Round
  - round() -> Retorna um número arredondado para n dígitos de precisão após a casa decimal.
Se a precisão não for informada retorna o inteiro mais próximo da entrada
"""

# Len
print(f'Quantidade de elementos da string: {len("Geek University")}')
print(f'Quantidade de elementos da lista: {len([1, 2, 3, 4, 5])}')
print(f'Quantidade de elementos da tupla: {len((1, 2, 3, 4, 5))}')
print(f'Quantidade de elementos do conjunto: {len({1, 2, 3, 4, 5})}')
print(f'Quantidade de elementos do dicionário: {len({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})}')
print(f'Quantidade de elementos do range: {len(range(0, 10))}')

# Quando utilizamos a função len() o Python faz o seguinte
print(f'Quantidade de elementos da string: {"Geek University".__len__()}')
# Dunder -> funções que tem 2 underline antes e 2 depois do nome da função

print("--------------------------------------------------")

# Abs
print(f'Número absoluto de -5: {abs(-5)}')
print(f'Número absoluto de 5: {abs(5)}')
print(f'Número absoluto de 3.14: {abs(3.14)}')
print(f'Número absoluto de -3.14: {abs(-3.14)}')

print("--------------------------------------------------")

# Sum
print(f'A soma da lista de números 1, 2, 3, 4, 5: {sum([1, 2, 3, 4, 5])}')
# passando valor inicial sum(iterável, valor_inicial)
print(f'A soma da lista de números 1, 2, 3, 4, 5, com valor inicial igual a 5: {sum([1, 2, 3, 4, 5], 5)}')
print(f'A soma da tupla de números 1, 2, 3, 4, 5: {sum((1, 2, 3, 4, 5))}')
print(f'A soma do conjunto de números 1, 2, 3, 4, 5: {sum({1, 2, 3, 4, 5})}')
print(f'A soma do dicionário de números 1, 2, 3, 4, 5: {sum({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}.values())}')
print(f'A soma da lista de números 3.145, 5.678: {sum([3.145, 5.678])}')

print("--------------------------------------------------")

# Round
print(f'round(10.2): {round(10.2)}')
print(f'round(10.2, 3): {round(10.2, 3)}')
print(f'round(10.5): {round(10.5)}')
print(f'round(10.6): {round(10.6)}')
print(f'round(1.2121212121, 2): {round(1.2121212121, 2)}')
print(f'round(1.219999, 5): {round(1.219999, 5)}')
