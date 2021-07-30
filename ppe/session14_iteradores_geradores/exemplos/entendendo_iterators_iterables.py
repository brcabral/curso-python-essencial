"""
Entendendo Iterators e Iterables

Iterator:
  - Um objeto que pode ser iterado
  - Um objeto que retorna um dado, sendo um elemento por vez, quando a função next() é chamada

Iterable:
  Um objeto que irá retornar um iterator quando a função iter() for chamada
"""

nome = 'Geek'
numeros = [1, 2, 3, 4, 5, 6]

print(f'Tipo da variável nome: {type(nome)}')
print(f'Tipo da variável numeros: {type(numeros)}')

it1 = iter(nome)
it2 = iter(numeros)

print(f'Tipo da variável nome (após conversão): {type(nome)}')
print(f'Tipo da variável numeros (após conversão): {type(numeros)}')

print()
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

"""
Quando iteramos um elemento o Python automaticamente converter o elemento.

Exemplo:
for letra in nome:  -> it1 = iter(nome)
    print(letra)    -> print(next(it1))
"""

print()
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
