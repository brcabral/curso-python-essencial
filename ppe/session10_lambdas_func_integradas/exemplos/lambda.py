"""
Lambdas
 - Conhecidas por Expressão Lambdas, ou simplemente Lambdas, são funções anônimas

"""


# Exemplo de função em Python
def funcao(x):
    return 3 * x + 1


print(f'Executando função(3): {funcao(3)}')
print(f'Executando função(4): {funcao(4)}')
print(f'Executando função(7): {funcao(7)}')

# Expressão Lambda
# lambda x: 3 * x + 1

# Como utilizar a expressão lambda
calc = lambda x: 3 * x + 1

print(f'Executando lambda calc(3): {calc(3)}')
print(f'Executando lambda calc(4): {calc(4)}')
print(f'Executando lambda calc(7): {calc(7)}')

print("--------------------------------------------------")
# Podemos ter expressões lambdas com múltiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(f'Executando lambda nome_completo: {nome_completo(" Julia ", " AMARAL    ")}')
print(f'Executando lambda nome_completo: {nome_completo("   carlos   ", "LORENZO  ")}')

print("--------------------------------------------------")
# Assim como em funções, em Lambdas podemos ter nenhuma ou várias entradas

amar = lambda: 'Como não amar Python?!'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)
# n = lambda x1, x2, ..., xn: <expressao>

print(f'Executando lambda amar(): {amar()}')
print(f'Executando lambda uma(6): {uma(6)}')
print(f'Executando lambda duas(5, 7): {duas(5, 7)}')
print(f'Executando lambda tres(3, 6, 9): {tres(3, 6, 9)}')

print("--------------------------------------------------")

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']
print(f'Lista de autores: {autores}')

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(f'Lista de autores ordenada por sobrenome: {autores}')

print("--------------------------------------------------")


# Função quadrática
# f(x) = a * x ** 2 + b * x + c

# Definindo a função
def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c


funcao = geradora_funcao_quadratica(2, 3, -5)

print(f'Executando função(0): {funcao(0)}')
print(f'Executando função(1): {funcao(1)}')
print(f'Executando função(2): {funcao(2)}')
print(f'Executando funcao_quadratica(3, 0, 1)(2): {geradora_funcao_quadratica(3, 0, 1)(2)}')
