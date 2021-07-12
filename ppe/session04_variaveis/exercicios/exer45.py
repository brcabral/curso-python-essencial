"""
Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela
ASCII para resovler o problema
"""

letra_minuscula = input('Digite uma letra maiúscula: ')
letra_ascii = ord(letra_minuscula)
letra_maiuscula = chr(letra_ascii + 32)
print(f'A letra minúscula digitada é: {letra_maiuscula}')
