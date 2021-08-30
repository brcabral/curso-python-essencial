"""
Novos metadata
"""

from importlib import metadata

print(metadata.version('pip'))

print("--------------------------------------------------")

metadados_pip = metadata.metadata('pip')
print(list(metadados_pip))
print(metadados_pip['Project-URL'])
print(metadados_pip['Author'])

print("--------------------------------------------------")

# Quantidade de arquivos no pacote
print(len(metadata.files('pip')))

print("--------------------------------------------------")

# Verifica quais pacotes extras são necessários
print(metadata.requires('pip'))
print(metadata.requires('mypy'))
