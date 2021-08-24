"""
O tipo ou a classe do objeto é menos importante do que os métodos que o definem
"""


class CisneNegro:
    def __len__(self):
        return 42


livro = CisneNegro()
print(f'Len de livro: {len(livro)}')

nome = 'Geek University'
lista = [12, 34, 55, 49]
dicio = {'carlos': 12, 'vanessa': 34, 'joana': 49}

print(f'Len de nome: {len(nome)}')
print(f'Len de lista: {len(lista)}')
print(f'Len de dicio: {len(dicio)}')

# Apesar das variáveis terem tipos diferentes, todas possuem o método len. Ou seja, elas são similares.
# Variáveis similares devem ter métodos, atributos ou comportamento similares.
