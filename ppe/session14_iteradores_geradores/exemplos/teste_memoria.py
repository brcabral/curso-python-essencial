"""
Teste de memória com Generators

Sequência de Fibonacci
  - 1, 1, 2, 3, 5, 8, 13, 21...
"""


def fib_lista(qtd_num):
    nums = []
    a, b = 0, 1
    while len(nums) < qtd_num:
        nums.append(b)
        a, b = b, a + b
    return nums


# Teste para verificar consumo de memória com 100000 elementos - 449MB
for n in fib_lista(100):
    print(n)

print("--------------------------------------------------")


def fib_gen(qtd_num):
    a, b, contador = 0, 1, 0
    while contador < qtd_num:
        a, b = b, a + b
        yield a
        contador = contador + 1


# Teste para verificar consumo de memória com 100000 elementos - 3.2MB
for n in fib_gen(100):
    print(n)
