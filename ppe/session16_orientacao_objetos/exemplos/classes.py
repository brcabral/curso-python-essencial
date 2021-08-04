"""
Classes
  -> são modelos do mundo real sendo representados computacionalmente.

Para definir uma classe usamos a palavra reservada class

Classes podem conter:
 - Atributos -> Representam as características do objeto, ou seja, pelos atributos conseguimos
representar computacionalmente os estados de um objeto.
 - Métodos -> Representam o comportamento do objeto, ou seja, as ações que este objeto pode realizar.


OBS.: Quando nomeamos nossas classes utilizamos por convenção o nome em maiúsculo.
Se o nome for composto, não separamos as palavra e utilizamos as iniciais de ambas
em maiúsculo (CamelCase)
"""


# Imagine que você queira fazer um sistema para automatizar o controle de lâmpadas da sua casa
class Lampada:
    pass


lamp = Lampada()
print(f'Tipo da variável lamp: {type(lamp)}')
