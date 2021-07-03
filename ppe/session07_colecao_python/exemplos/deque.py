"""
Módulo Collections - Deque
https://docs.python.org/3/library/collections.html#collections.deque

É uma lista de alta performance
"""
# Fazendo o import
from collections import deque

# Criando deques
deq = deque('geek')
print(f'deq: {deq}')

# Adicionando elementos no deque

# append -> adiciona o elemento no final
deq.append('y')
print(f'deq após append: {deq}')

# appendleft -> adiciona o elemento no início
deq.appendleft('x')
print(f'deq após appendleft: {deq}')

# Remover elementos do deque
# pop -> Remove e retorna o último elemento
print(f'elemento removido (pop): {deq.pop()}')
print(f'deq após pop: {deq}')

# popleft -> Remove e retorna o primeiro elemento
print(f'elemento removido (popleft): {deq.popleft()}')
print(f'deq após popleft: {deq}')
