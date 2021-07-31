"""
Teste de velocidade com Expressões Geradores
"""
# Generator


def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()
print(ge1)  # Generator

print(next(ge1))
print(next(ge1))

print("--------------------------------------------------")
# Generator Expression

ge2 = (num for num in range(1, 10))

print(ge2)  # Generation Express

print(next(ge2))
print(next(ge2))

print("--------------------------------------------------")

# Teste de velocidade
import time

# Generator Expression
gen_inicio = time.time()
print(sum(num for num in range(100_000_000)))
gen_tempo = time.time() - gen_inicio


# List Comprehension
list_inicio = time.time()
print(sum([num for num in range(100_000_000)]))
list_tempo = time.time() - list_inicio

print(f'Tempo gasto pelo Generation Express: {gen_tempo}')  # 5.7s
print(f'Tempo gasto pelo List Comprehension: {list_tempo}')  # 19.3s
