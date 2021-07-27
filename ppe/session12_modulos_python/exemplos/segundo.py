import primeiro


def funcao2():
    primeiro.funcao1()


if __name__ == '__main__':
    funcao2()
    print('segundo.py está sendo executado diretamente')
else:
    print(f'valor da variável __name__: {__name__}')
    print('segundo.py foi importado')
