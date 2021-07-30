"""
Geradores
  - Geradores (Generators) são iteradores (Iterators)
  - Generators podem ser criados com funções geradoras
  - Funções geradoras utilizam a palavra reservada yield
  - Generators podem ser criados com Expressões Geradoras

Diferenças entre funções e generator functions (funções geradoras)

-----------------------------------------------------------------------------------------
| Funções                                   | Generator Functions                       |
-----------------------------------------------------------------------------------------
| utilizam return                           | utilizam yield                            |
-----------------------------------------------------------------------------------------
| possuem apenas um retorno                 | podem ter vários yield                    |
-----------------------------------------------------------------------------------------
| quando executada, retorna um valor        | quando executada, retorna um generator    |
-----------------------------------------------------------------------------------------

"""
# Exemplo função geradora (Generator function)
# OBS.: Um generator function não é um Generator, ela gera um generator


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


gen = conta_ate(5)
print(f'Tipo da variável gen: {type(gen)}')

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print("--------------------------------------------------")

gen_conta = conta_ate(10)
for num in gen_conta:
    print(num)

print("--------------------------------------------------")

numeros_gen = list(conta_ate(10))
print(numeros_gen)
