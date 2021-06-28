"""
Tripo string

Em Python, um dado é considerado string sempre que:
 - Estiver entre aspas simples;
 - Estiver entre aspas duplas;
 - Estiver entre aspas simples triplas;
 - Estiver entre aspas duplas triplas;
"""

nome = 'Geek University'
print(f'Variável nome = {nome}')
print(f'Tipo da variável nome = {type(nome)}')

local = "Gina's Bar"
print(f'Variável local = {local}')
print(f'Tipo da variável local = {type(local)}')

# Para quebrar linha podemos usar \n
nome = "Geek \nUniversity"
print(f'Variável nome = {nome}')
print(f'Tipo da variável nome = {type(nome)}')

# Ou atribuir o valor usando aspas tripla e escrever pulando linha
nome = """Geek
University"""
print(f'Variável nome = {nome}')
print(f'Tipo da variável nome = {type(nome)}')

nome = "Geek University"
print(f'Variável nome = {nome}')
print(f'Variável nome.upper() = {nome.upper()}')
print(f'Variável nome.lower() = {nome.lower()}')
print(f'Variável nome.split() = {nome.split()}')
print(f'Variável nome.split()[0] = {nome.split()[0]}')
print(f'Variável nome.split()[1] = {nome.split()[1]}')

nome_curso = "Geek University, Programação em Python"
print(f'Variável nome_curso = {nome_curso}')
print(f'Variável nome_curso.split(",") = {nome_curso.split(",")}')

# Slice de string
# Imprimir partes da string [posição inicial: posição final - 1]
print(f'Variável nome = {nome}')
print(f'Variável nome[0:4] = {nome[0:4]}')
print(f'Variável nome[5:15] = {nome[5:15]}')

# [::-1] -> Comece do primeiro elemento (:), vá até o último (:) e inverta (-1)
print(f'Variável nome[::-1] = {nome[::-1]}')

print(f'Variável nome.replace("e", "i") = {nome.replace("e", "i")}')

# palíndromo
texto = "socorram me subino onibus em marrocos"
print(f'Variável texto = {texto}')
print(f'Variável texto[::-1] = {texto[::-1]}')
