"""
Debugando com Python Debugger

Podemos fazer debug em diferentes IDEs, como o PyChar ou utilizando o PDB
"""
# Para utilizar o Python Debugger, precisamos importar a biblioteca pdb e utilizar a função set_trace()
import pdb

"""
Comandos básicos do PDB
  - l -> listar trecho do código
  - n -> próxima linha
  - [p] <nome_variavel> -> imprime valor da variável
  - c -> continua a execução (até o próximo set_trace ou o final do código)
  - h -> help
"""

nome = 'Maria'
sobrenome = 'Aparecida'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação Python: Essencial'
pdb.set_trace()
final = nome_completo + ' faz o curso ' + curso
print(final)

print("--------------------------------------------------")

# A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug
# foi incorporada como função built-in chamada breakpoint()

nome = 'Maria'
sobrenome = 'Aparecida'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação Python: Essencial'
breakpoint()
final = nome_completo + ' faz o curso ' + curso
print(final)
