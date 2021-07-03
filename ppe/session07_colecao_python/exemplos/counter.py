"""
Módulo Collections - Counter
Collections -> High-performance Container Datetypes
https://docs.python.org/3/library/collections.html#collections.Counter

Counter
 - Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter
que é parecido com um dicionário, contendo como chave o elemento da lista passada
como parâmetro e como valor a quantidade de ocorrências desse elemento.
"""
# Importando o Counter
from collections import Counter

# Podemos utilizar qualquer iterável, nesse caso usamos uma Lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 2, 12, 7, 8, 5, 3, 8, 9, 10, 6, 8, 7, 2, 4, 25, 27, 30]

# Utilizando o counter
counter = Counter(lista)
print(f'Conjunto counter: {counter}')
print(f'Tipo da variável counter = {type(counter)}')

# Counter({3: 5, 1: 4, 2: 4, 8: 3, 7: 2, 12: 1, 5: 1, 9: 1, 10: 1, 6: 1, 4: 1, 25: 1, 27: 1, 30: 1})
# Para cada elemento da lista, o Counter criou uma chave e como valor o total de ocorrências

print('--------------------------------------------------')
# Gerando um Counter através de uma string
print(f'Counter de uma string: {Counter("Geek University")}')

print('--------------------------------------------------')
#
texto = """A Wikipédia é um projeto de enciclopédia colaborativa, universal e multilíngue estabelecido na internet 
sob o princípio wiki. Tem como propósito fornecer um conteúdo livre, objetivo e verificável, que todos possam editar 
e melhorar. O projeto é definido pelos princípios fundadores e o conteúdo é disponibilizado sob a licença Creative 
Commons BY-SA e pode ser reutilizado sob a mesma licença, desde que respeitando os termos de uso. Todos podem 
publicar conteúdo on-line desde que criem uma conta e sigam as regras básicas, como verificabilidade ou notoriedade. 

Todos os editores da Wikipédia são voluntários e integram uma comunidade colaborativa, sem um líder, onde coordenam 
esforços em projetos temáticos e espaços de discussão. Dentre as várias páginas de ajuda à disposição, estão as que 
explicam como criar um artigo ou editar um artigo. Em caso de dúvidas, não hesite em perguntar. Debates e comentários 
sobre os artigos são bem-vindos. As páginas de discussão servem para centralizar reflexões e avaliações sobre como 
melhorar o conteúdo da Wikipédia. """

palavras = texto.split()
print(f'Lista de palavras: {palavras}')

counter = Counter(palavras)
print(f'Counter de palavras: {counter}')

# Encontrar as 5 palavras com mais ocorrências no texto
print(f'As 5 palavras mais usadas no texto: {counter.most_common(5)}')
