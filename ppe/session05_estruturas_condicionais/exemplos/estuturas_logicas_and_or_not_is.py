"""
Estruturas lógicas
and, or, not, is

Operadores unários:
 - not
Operadores binários:
 - and, or, is
"""

ativo = True

if ativo:
    print("Usuário ativo no sistema")

print("--------------------------------------------------")

ativo = True
logado = True

if ativo and logado:
    print("Bem-vindo usuário")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")

print("--------------------------------------------------")

ativo = False
logado = True

if ativo and logado:
    print("Bem-vindo usuário")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")

print("--------------------------------------------------")

ativo = True
logado = True

if ativo or logado:
    print("Bem-vindo usuário")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")

print("--------------------------------------------------")

ativo = True
logado = False

if ativo or logado:
    print("Bem-vindo usuário")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")

print("--------------------------------------------------")

ativo = False
logado = False

if ativo or logado:
    print("Bem-vindo usuário")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")

print("--------------------------------------------------")

ativo = True

# Se não estiver ativo
if not ativo:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")
else:
    print("Bem vindo usuário")

print("--------------------------------------------------")
ativo = True
logado = True

# if (not ativo) and logado:
if not ativo and logado:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")
else:
    print("Bem vindo usuário")

print("--------------------------------------------------")

numero = 1
print(f'Tipo da variável numero = {type(numero)}')

if type(numero) is int:
    print("O número é inteiro")
else:
    print("O número não é inteiro")

print("--------------------------------------------------")

nome = "Python"
print(f"nome.islower() = {nome.islower()}")
print(f"nome.isupper() = {nome.isupper()}")
print(f"nome.istitle() = {nome.istitle()}")
print(f"nome.upper().isupper() = {nome.upper().isupper()}")
