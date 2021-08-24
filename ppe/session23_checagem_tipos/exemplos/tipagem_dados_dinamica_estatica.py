# Tipagem dinâmica
idade = 42
print(f'Tipo da variável idade: {type(idade)}')

idade = 'Quarenta e dois'
print(f'Tipo da variável idade: {type(idade)}')


print("--------------------------------------------------")

if False:
    resultado = 1 + 'Geek'
else:
    resultado = 1 + 41

print(f'O resultado é: {resultado}')
