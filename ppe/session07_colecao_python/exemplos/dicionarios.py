"""
Dicionários

OBS.: Em alguma linguagens de programação, os dicionários Python são conhecidos por mapas.
Dicionários são coleções do tipo chave/valor.

Sobre os dicionários:
 1 - Os dicionários são representadas por chaves {}
 2 - Tanto chave quanto o valor podem ser de qualquer tipo de dados
 3 - Podemos misturar tipos de dados
 4 - Em dicionários NÃO podemos ter chaves repetidas
"""
# Exemplo de declaração e exibição

# Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(f'Dicionário paises: {paises}')
print(f'Tipo do dicionário paises = {type(paises)}')

# Forma 2 (Menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(f'Dicionário paises: {paises}')
print(f'Tipo do dicionário paises = {type(paises)}')

print('--------------------------------------------------')
# Acessando os elementos
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Forma 01 - Acessando via chave
# OBS.: Ao tentar acessar uma chave que não existe, será apresentado um erro (KeyError)
print(f'Pais com a chave BR: {paises["br"]}')
print(f'Pais com a chave PY: {paises["py"]}')

# Forma 02 - Acessando via get (forma recomendada)
# OBS.: Ao tentar acessar uma chave que não existe, será retornado None (sem tipo de dado)
print(f'Pais com a chave BR: {paises.get("br")}')
print(f'Pais com a chave RU: {paises.get("ru")}')

russia = paises.get('ru')
if russia:
    print('Encontrei a Rússia')
else:
    print('Não encontrei a Rússia')

brasil = paises.get('br')
if brasil:
    print('Encontrei o Brasil')
else:
    print('Não encontrei o Brasil')

# Com o get, podemos definir um valor padrão caso não a chave informada não exista
portugual = paises.get('pt', 'Pais não encontrado')
print(f'Pais com a chave PT: {portugual}')

print('--------------------------------------------------')
#  Verificar se determinada CHAVE está no dicionário
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(f'A chave BR está no dicionário: {"br" in paises}')
print(f'A chave RU está no dicionário: {"ru" in paises}')
print(f'A chave Estados Unidos está no dicionário: {"Estados Unidos" in paises}')

# Exemplo, utilizando o in, para acessar um valor no dicionário
if 'ru' in paises:
    russia = paises['ru']

print('--------------------------------------------------')
# Podemos utilizar qualquer tipo de dado (int, float, string, boolean) inclusive lista, tupla
# como chave de um dicionário

# É interessante usar tuplas como chave nos dicionários, por elas são imutáveis
localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(f'Dicionário localidades: {localidades}')
print(f'Tipo do dicionário localidades = {type(localidades)}')

print('--------------------------------------------------')
# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(f'Dicionário receita: {receita}')

# Forma 01 - Mais comum
receita['abr'] = 350
print(f'Dicionário receita: {receita}')

# Forma 02
novo_dado = {'mai': 500}
receita.update(novo_dado)
receita.update({'jun': 700})
print(f'Dicionário receita: {receita}')

# Atualizando dados em um dicionário
print('>>>>> Atualizando dados <<<<<')

# Forma 01
receita['mai'] = 550
print(f'Dicionário receita: {receita}')

# Forma 02
receita.update({'jun': 750})
print(f'Dicionário receita: {receita}')

# CONCLUSÃO 1: Podemos utilizar as mesmas formas para adicionar ou alterar um elemento
# CONCLUSÃO 2: Em dicionários NÃO podemos ter chaves repetidas

print('--------------------------------------------------')
# Remover dados de um dicionário

estados = {'es': 'Espirito Santo', 'mg': 'Minas Gerais', 'rj': 'Rio de Janeiro', 'sp': 'São Paulo',
           'pr': 'Parana', 'sc': 'Santa Catarina', 'rs': 'Rio Grande do Sul'}
print(f'Dicionário estados: {estados}')

# Forma 1 - Mais comum
# Caso não exista a chave informada será apresentado um erro (KeyError)
# Ao remover um elemento, o valor desse elemento é retornado
retorno = estados.pop('rj')
print(f'Estado removido: {retorno}')
print(f'Dicionário estados: {estados}')

# Forma 2
# Caso não exista a chave informada será apresentado um erro (KeyError)
# Dessa forma não é possível obter o valor excluído
del estados['mg']
print(f'Dicionário estados: {estados}')

print('--------------------------------------------------')
# Cópia de dicionários
estados = {'es': 'Espirito Santo', 'mg': 'Minas Gerais', 'rj': 'Rio de Janeiro', 'sp': 'São Paulo'}

"""
Assim como nas listas podemos copiar a lista por Shallow Copy Deep Copy
 - Shallow = Cópia por atribuíção (dicionários compartilhados)
 - Deep = Cópia através do método copy (dicionários independentes)
"""

print(f'Dicionário estados: {estados.items()}')

copia = estados
# copia = estados.copy()
print(f'Dicionário copia: {copia}')

copia.update({'se': 'Sergipe'})
print(f'Dicionário estados: {estados}')

print('--------------------------------------------------')
# Limpar um dicionário
dic_numeros = dict(a=1, b=2, c=3)
print(f'Dicionário dic_numeros: {dic_numeros}')

dic_numeros.clear()
print(f'Dicionário dic_numeros apos clear: {dic_numeros}')

print('--------------------------------------------------')
# Forma não usual de criar dicionários

novo_dic = {}.fromkeys('a', 'b')
print(f'Dicionário novo_dic: {novo_dic}')

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(f'Dicionário usuario: {usuario}')

"""
- O método fromkeys recebe dois paramêtros: um iterável e um valor
- Ele vai gerar para cada valor do iterável uma chave e irá atribuir a estar chave o valor informado.
"""
dicionario = {}.fromkeys('teste', 'valor')
print(f'Dicionário dicionario: {dicionario}')

dicionario = {}.fromkeys(range(1, 11), 'novo')
print(f'Dicionário dicionario: {dicionario}')
