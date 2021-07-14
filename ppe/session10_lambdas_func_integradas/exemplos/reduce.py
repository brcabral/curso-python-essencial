"""
Reduce

OBS.: A partir do Python 3+ a função reduce() não é mais uma função integrada (built-in). Agora temos
que importar esta função a partir do módulo functools

Guido Van Rossum (criador do Python): Utilize a função reduce() se você realmente precisar dela.
Em 99% dos casos um loop for é mais legível

# Para entender o reduce()
# Coleção de dados
dados = [a1, a2, a3, ..., aN]

# Temos uma função que recebe dois parâmetros
def funcao(x, y):
    return x * y

# O reduce() também recebe dois parâmetros, sendo uma função e um iterável
reduce(funcao, dados)

# A função reduce(), funciona da seguinte forma:
  # Passo 1: result1 = f(a1, a2) -> Aplica a função nos dois primeiros elementos da coleção e guarda o resultado
  # Passo 2: result2 = f(result1, a3) -> Aplica a função passando o resultado do passo1 mais o terceiro elemento
  #          e guarda o resultado
  # Isso é repetido até o final
  # Passo n: resultN = f(resultM, aN)

Ou seja, em cada passo ele aplica a função passando como primeiro argumento o resultado da aplicação anterior.
No final, reduce() irá retornar o resultado final.
"""

# Utilizando a função reduce() para multiplicar todos os números de uma lista

# Importando o reduce de functools
from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

result = reduce(lambda x, y: x * y, dados)
print(f'A multiplicação de todos os números é: {result}')
