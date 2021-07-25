"""
Try / Except / Else / Finally

Else -> É executado somente se não ocorrer o erro.
  - Podemos ter apenas 1 else, depois do tratamento de todas as exceções

Finally -> O bloco finally SEMPRE é executado. Independente se houver ou não uma exceção.
  - O finally, geralmente, é utilizado para fechar ou desalocar recursos.

Dica de quando e onde tratar o código.
  - Toda entrada de dados deve ser tratada
"""

try:
    num = int(input('Digite um número inteiro: '))
except ValueError:
    print('Valor digitado incorreto')
else:
    print(f'Você digitou o número: {num}')

print("--------------------------------------------------")

try:
    num = int(input('Digite um número inteiro: '))
except ValueError:
    print('Valor digitado incorreto')
else:
    print(f'Você digitou o número: {num}')
finally:
    print('Executando o finally')

print("--------------------------------------------------")


def dividir(a, b):
    try:
        return f'O resultado da divisão de {a} / {b} é: {int(a) / int(b)}'
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível dividir por zero'


num1 = input('Digite o primeiro número inteiro: ')
num2 = input('Digite o segundo número inteiro: ')
print(dividir(num1, num2))

print("--------------------------------------------------")


def dividir(a, b):
    try:
        return f'O resultado da divisão de {a} / {b} é: {int(a) / int(b)}'
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


num1 = input('Digite o primeiro número inteiro: ')
num2 = input('Digite o segundo número inteiro: ')
print(dividir(num1, num2))
