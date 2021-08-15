"""
Métodos mágicos
 -> São todos os métodos que utilizam dunder (Double Underscore)

ex.: __init__
"""


class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        """
          Representa a forma como será exibido as informações do objeto

          como executar: print(livro1)
          ex. com repr padrao: <__main__.Livro object at 0x7f26b9d31f10>
          ex. com repr atual: Python Rocks!, escrito por Geek University
        """
        return f'{self.titulo}, escrito por {self.autor}'

    def __str__(self):
        """
          Semelhante ao repr, irá exibir as informações do objeto.
          O método str tem prioridade sobre o repr

          como executar: print(livro1)
          ex. com str padrao: <__main__.Livro object at 0x7f26b9d31f10>
          ex. com str atual: O título do livro é Python Rocks!
        """
        return f'O título do livro é {self.titulo}'

    def __len__(self):
        """
          Sobrescrever o método len.
          O retorno precisa ser um inteiro
        """
        return self.paginas

    def __del__(self):
        """
          Não altera o funcionamento do del, mas irá adicionar novos comportamentos.
          Nesse exemplo vai exibir uma mensagem informando da exclusão do objeto
        """
        print('Um objeto do tipo livro foi excluído da memória')

    def __add__(self, other_book):
        """
          Sobrescrever o método add para concatenar o título de dois livros.
        """
        return f'{self.titulo} - {other_book.titulo}'

    def __mul__(self, quantidade):
        """
          Sobrescrever o métodos mul para permitir executar uma múltiplição entre um objeto e um inteiro
        """
        if isinstance(quantidade, int):
            msg = ''
            for n in range(quantidade):
                msg += ' ' + str(self) + ' | '
            return msg
        return 'Não foi possível executar o método. É preciso passar um inteiro no segundo parâmetro'


livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial em Python!', 'Geek University', 350)

print(livro1)
print(livro2)

print("--------------------------------------------------")

print(f'Quantidade de páginas livro1: {len(livro1)}')
print(f'Quantidade de páginas livro2: {len(livro2)}')

print("--------------------------------------------------")

livro3 = Livro('Livro para teste', 'Geek University', 127)
del livro3

"""
OBS.: Ao finaliza a execução do programa, o Python excluí todas as variáveis da memória
Por isso será exibida várias vezes a mensagem "Um objeto do tipo livro foi excluído da memória"
no console.
"""

print("--------------------------------------------------")

print(livro1 + livro2)

print("--------------------------------------------------")

print(livro1 * 3)

print("--------------------------------------------------")
