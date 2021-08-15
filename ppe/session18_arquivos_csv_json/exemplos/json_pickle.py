"""
JSON e Pickle
 - JSON -> JavaScript Object Notation
"""

import json

# Dumps: Prepara os dados para o formato JSON (acerta colchete, chaves, aspas)
import jsonpickle

ret = json.dumps(['produto', {'PlayStation 4': ('2TB', 'Novo', '110V', 2340)}])
print(f'Tipo da variável gato: {type(ret)}')
print(f'Ret: {ret}')

print("--------------------------------------------------")


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'SRD')
print(f'felix_json: {felix.__dict__}')
felix_json = json.dumps(felix.__dict__)
print(f'felix_json: {felix_json}')

print("--------------------------------------------------")

# Integrando o JSON com Pickle
"""
Para fazer essa integração usamos a biblíoteca jsonpickle
para instalar: pip install jsonpickle
"""

encode_felix = jsonpickle.encode(felix)
print(f'encode_felix: {encode_felix}')

print("--------------------------------------------------")

# Escrevendo o arquivo json/pickle
with open('arquivos/felix.json', 'w') as arquivo:
    felix_json = jsonpickle.encode(felix)
    arquivo.write(felix_json)

print("--------------------------------------------------")

# Lendo um arquivo json/pickle
with open('arquivos/felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    gato_json = jsonpickle.decode(conteudo)
    print(f'gato_json: {gato_json}')
    print(f'Tipo da variável gato: {type(gato_json)}')
    print(f'nome: {gato_json.nome}')
    print(f'raça: {gato_json.raca}')
