"""
Módulos externos
  Utilizamos o gerenciador de pacotes Pyton chamado PIP (Python Installer Package)
  Digite pip no terminal para visualizar os comandos e opções de uso

Os pacotes externos oficiais estão em: https://pypi.org/
"""

import pydf

pdf = pydf.generate_pdf('<h1>Geek University</h1><br/><br/><string>'
                        'Programa&ccedil;&atilde;o em Python: Essencial</strong>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
