"""
Assertions
 - Em Python utilizamos a palavra reservada assert para realizar afirmações utilizadas nos testes
 - Utilizamos o assert em uma expressão que queremos verificar se é válida ou não. Se for verdadeira,
retorna None e caso seja falsa lança um erro do tipo AssertionErro.
 - É possível especificar um segundo argumento ou uma mensagem de erro erro personalizada.
 - A palavra assert pode ser utilizada em qualquer função ou código, não precisa ser exclusivamente
nos testes

ATENÇÃO!!!
 - Se um programa for executado com a parâmetro -O (menos o maiúsculo), nenhum assertion será validado.
Ou seja, todas as validações não serão feitas
"""


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b


ret1 = soma_numeros_positivos(2, 4)  # 6
print(f'soma_numeros_positivos(2, 4): {ret1}')

# ret2 = soma_numeros_positivos(-2, 4)  # AssertionError
# print(f'soma_numeros_positivos(-2, 4): {ret2}')

print("--------------------------------------------------")


def comer_fast_foot(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente',
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'


comida = 'sorvete'
print(comer_fast_foot(comida))
