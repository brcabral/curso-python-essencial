"""
Generators Expression

Em aulas anteriores estudamos:
 - List Comprehension
 - Dictionary Comprehension
 - Set Comprehension

Mas não vimos o Tuple Comprehension, porque eles se chamam Generators
"""

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

# List Comprehension
list_comprehension = [nome[0] == 'C' for nome in nomes]
print(f'Variável nome = {list_comprehension}')
print(f'Tipo da variável list_comprehension: {type(list_comprehension)}')

print()

# Generator
generator = (nome[0] == 'C' for nome in nomes)
print(f'Variável nome = {generator}')
print(f'Tipo da variável generator: {type(generator)}')

print("--------------------------------------------------")

"""
OBS.: O generator é mais performático do que o List/Dictionary/Set Comprehension
Portanto quando não for necessário o uso específico de um dos comprehensions,
dar preferência para o Generator
"""

"""
Por exemplo, caso queira saber na lista há algum nome que inicia com a letra C
podemos usar o Generator, pois o resultado será o mesmo, porém o código terá uma
performance melhor.
"""

print(f'Algum nome começam com C (list_comprehension)? {any([nome[0] == "C" for nome in nomes])}')
print(f'Algum nome começam com C (generator)? {any(nome[0] == "C" for nome in nomes)}')

print("--------------------------------------------------")

from sys import getsizeof

# getsizeof() -> Retorna a quantidade de bytes que o elemento passado como parâmetro ocupa
print(f'String Geek: {getsizeof("Geek")}')
print(f'String University: {getsizeof("University")}')
print(f'Numero 9: {getsizeof(9)}')
print(f'Numero 91: {getsizeof(91)}')
print(f'Numero 92345668823: {getsizeof(92345668823)}')
print(f'Boolean True: {getsizeof(True)}')

print("--------------------------------------------------")

# Gerando uma lista de números com List Comprehension
list_comprehension = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comprehension = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension
dictionary_comprehension = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator Expression
generator_expression = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória...')
print(f'List Comprehension: {list_comprehension} bytes.')
print(f'Set Comprehension: {set_comprehension} bytes.')
print(f'Dictionary Comprehension: {dictionary_comprehension} bytes.')
print(f'Generator Expression: {generator_expression} bytes.')

print("--------------------------------------------------")

# Iterando o Generator Express
numeros = (x * 10 for x in range(100))
print(f'Tipo da variável numeros: {type(numeros)}')

for num in numeros:
    print(num)
