"""
Sintaxe perigosas (SyntaxWarning)
 - Exibe um alerta sobre possíveis erros de síntaxe, informando a possível problema.
"""

versao = '3.8'
# SyntaxWarning: "is" with a literal. Did you mean "=="?
if versao is '3.8':
    print('Igual')
else:
    print('Diferente')

print("--------------------------------------------------")

# SyntaxWarning: 'str' object is not callable; perhaps you missed a comma?
lista = [('Geek') ('University')]
print(lista)
