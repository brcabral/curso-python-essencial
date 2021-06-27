## Instalar Python no Linux

- Instalar as dependências
`sudo apt install build-essential zlib1g-dev libjpeg-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev sqlite3 liblzma-dev curl libbz2-dev`

- Baixar o fonte do Python
    - https://www.python.org/downloads/

- Descompactar o Python baixado

- Com o terminal aberto no diretório do fonte executar
`./configure --enable-optimizations --with-ensurepip=install`

- Compilar fonte do Python
`make -j 2`

- Instalar o Python
`sudo make altinstall`

- Verificar a versão do Python instalada
`python3.x --version`
`pip3.x --version`

- Atualizar o pip
`sudo pip3.8 install --upgrade pip`
