def funcao1():
    print('Geek University - primeiro.py')


if __name__ == '__main__':
    funcao1()
    print('primeiro.py está sendo executado diretamente')
else:
    print(f'valor da variável __name__: {__name__}')
    print('primeiro.py foi importado')
