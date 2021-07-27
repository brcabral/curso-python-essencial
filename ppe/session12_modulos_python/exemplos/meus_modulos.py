def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27),
           ('Nova York', 28), ('Londres', 22)]

# Converterndo a temperatura para Fahrenheit
c_para_f = lambda dado: (dado[0], (9 / 5) * dado[1] + 32)


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(f'Somando a lista: {soma_impares(lista)}')

    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(f'Somando a tupla: {soma_impares(tupla)}')
else:
    print('O módulo meus_modulos.py foi importado.')
