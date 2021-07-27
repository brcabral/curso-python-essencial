"""
Dunder -> Double Under (Underscores)

Dunder Name
  __name__

Dunder Main
  __main__

Os dunder são utilizados para criar funções, atributos, propriedades, etc para não gerar
conflito com os nomes desse elementos na programação

Em Python, se executarmos um módulo diretamente na linha de comando, internamente o Python
atribuirá à variável __name__ o valor __main__ indicando que este módulo é o módulo
de execução principal

"""
from meus_modulos import soma_impares
print(f'Executando a função soma_impares de meus_modulos: {soma_impares([1, 2, 3, 4, 5, 6])}')

print("--------------------------------------------------")

import primeiro
import segundo
