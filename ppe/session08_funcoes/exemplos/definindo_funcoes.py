"""
Definindo funções

 - Funções são pequenas partes de código que realizam tarefas específicas;
 - Funções podem ou não receber entradas de dados e retornar uma saída;
 - Muito úteis para executar procedimentos similares por repetidas vezes;

OBS.: Se você escrever uma função que realiza várias tarefas; é recomendável
verificar o código, para que a função seja simplificada.
"""
# Exemplo de utilização de funções

curso = 'Programação em Python: Essencial'
cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (built-in) print()
print(f'Imprimindo a variável curso: {curso}')
print(f'Imprimindo a lista cores: {cores}')

# Utilizando a função append() -> função está atrelada as listas
# Recebe um parâmetro e não retorna dados
cores.append('roxo')

# Utilizando função clear() -> função está atrelada as listas
# Não recebe parâmetro e não retorna dados
cores.clear()
print(f'Imprimindo a lista cores: {cores}')

"""
DRY - Don't Repeat Yourself - Não repita seu código

Como definir uma função em Python
def nome_da_funcao(parametro_de_entrada):
    bloco_de_funcao

Onde:
 - nome_da_funcao
   - Deve ser sempre com letra minúscula;
   - Se for nome composto separar com underline (Snake case);
 - parametro_de_entrada
   - Pode ter zero ou N, em caso de mais um, serão separados por vírgula
 - bloco_da_funcao
   - É onde ocorre o processamento. Pode ou não ter o retorno de informações

OBS.: Para definir uma função, utilizamos a palavra reservada 'def'.
"""

print("--------------------------------------------------")


# Exemplo 01
# Definição da função
def diz_oi():
    print('oi!!')


# Utilizando nossa função
diz_oi()

print("--------------------------------------------------")


# Exemplo 02
def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de de vida')
    print('Viva o aniversariante!')


cantar_parabens()

print("--------------------------------------------------")
# Em Python, podemos criar variáveis do tipo de uma função e executar esta função através da variável
# Não colocar o parênteses ao atribuir a função na variável
canta = cantar_parabens
canta()

print()
print(f'Tipo da variável canta = {type(canta)}')
