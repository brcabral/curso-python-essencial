"""
Escopo de variáveis

Dois casos de escopo:
1 - Variáveis globais
    - Variáveis globais são reconhecidas em todo o programa

2 - Variáveis locais
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas
"""

"""
Python é uma linguagem de tipagem dinâmica.
Isso significa que ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor à mesma

Diferente de C e Java
int numero = 42;
"""

numero = 42 # Variável global
print(f'Variável numero = {numero}')
print(f'Tipo da variável numero = {type(numero)}')

numero = 'Geek University'
print(f'Variável numero = {numero}')
print(f'Tipo da variável numero = {type(numero)}')

num = 5
print(f'Variável num = {num}')

# novo -> variável local
if num > 10:
    novo = num + 10
    print(novo)

print(novo)
