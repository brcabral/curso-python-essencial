"""
Loop for
Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplo de iteráveis:
- String
  - nome = "Geek University"
- Lista
  - lista = [1, 3, 5, 7, 9]
- Range
  - numeros = range(1, 10)
"""

nome = "Geek University"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

# Exemplo de for 1 - Iterando em uma string
for letra in nome:
    print(letra)

# Exemplo de for 2 - Iterando sobre uma lista
for numero in lista:
    print(numero)

# Exemplo de for 3 - Iterando sobre um range
"""
range(valor_inicial, valor_final)
Obs.: O valor final não é inclusive.
"""
for numero in numeros:
    print(numero)

print("--------------------------------------------------")

"""
Enumerate:
(indice, letra)
((0, "G"), (1, "e"), (2, "e"), (3, "k"), (4, " "), (5, "U")...)
"""
for indice, letra in enumerate(nome):
    print(nome[indice])

print("--------------------------------------------------")

for indice, letra in enumerate(nome):
    print(letra)

print("--------------------------------------------------")
"""
O underline indica que o primeiro valor, ou seja o índice, está sendo descartado
Quando não precisamos de um valor, podemos descartá-lo utilizando o underline
"""
for _, letra in enumerate(nome):
    print(letra)

print("--------------------------------------------------")

for valor in enumerate(nome):
    print(valor)

print("--------------------------------------------------")

for valor in enumerate(nome):
    print(valor[0])

print("--------------------------------------------------")

for valor in enumerate(nome):
    print(valor[1])

print("--------------------------------------------------")

qtd = int(input("Quantas vezes esse loop deve rodar? "))

for n in range(1, qtd + 1):
    print(f"Imprimindo {n}")

print("--------------------------------------------------")

soma = 0

for n in range(1, qtd + 1):
    num = int(input(f"Informe o {n}/{qtd} valor: "))
    soma = soma + num

print(f"A soma é {soma}")

print("--------------------------------------------------")

for letra in nome:
    print(letra, end=" - ")

print("--------------------------------------------------", end='\n')

# Repetir o valor de uma string
print("Python " * 3)

print("--------------------------------------------------")
"""
Tabela de emojis: https://apps.timwhitlock.info/emoji/tables/unicode

Original: U+1F63B
Modificado: U0001F63B
"""

for _ in range(3):
    for num in range(1, 11):
        print("\U0001F63B" * num)
