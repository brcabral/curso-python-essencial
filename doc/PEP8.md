## PEP8 - Python Enhancement Proposal
São propostas de melhorias para a linguagem Python  
A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica  

1. Utilize Camel Case para nomes de classes
2. Utilize nomes em minúsculo, separado por underline para funções ou variáveis
3. Utilize 4 espaços para identação!!! (NÃO use tab)
4. Linhas em branco  
4.1 Separar funções e definições declasse com duas linhas em branco;  
4.2 Métodos dentro de uma classe devem ser separados com uma única linha em branco;
5. Imports devem ser sempre feitos em linhas separadas  
5.1 Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e antes de constantes ou variáveis globais
 - Errado
```
import sys, os
```

 - Certo
```
import sys
import os
```

 - Pode ser utilizado (max 3)
```
from types import StringType, ListType
```

 - Para mais de 3 imports
```
from types import (
	StringType,
	ListType,
	SetType,
	OutroType
)
```

6. Espaços em expressões e instruções
 - Errado
```
funcao( algo[ 1 ], { outro: 2 } )
algo (1)
dict ['chave'] = list [indice]
y  =  0
variavel_longa =   0
```

 - Certo
```
funcao(algo[1], {outro: 2})
algo(1)
dict['chave'] = list[indice]
y = 0
variavel_loga = 0
```

7. Termine sempre um arquivo com uma linha em branco após o fim do código
