"""
Documentando funções com Docstrings

 - Podemos ainda acessar a documentação através da função help()
 - Podemos ter acesso a documentação de uma função utilizando a propriedade __doc__
"""


def diz_oi():
    """Uma função simples que retorna s string 'Oi!'"""
    return 'Oi!'


print('>>>>> usando o método help <<<<<')
help(diz_oi)

print('>>>>> usando a propriedade __doc__ <<<<<')
print(diz_oi.__doc__)

print("--------------------------------------------------")


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' a 'potencia' informada
    :param numero:Número que deesejamos gerar o exponencial
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2
    :return: Retorna o exponencial de 'numero' por 'potencia'
    """
    return numero ** potencia


print('>>>>> usando o método help <<<<<')
help(exponencial)

print('>>>>> usando a propriedade __doc__ <<<<<')
print(exponencial.__doc__)
