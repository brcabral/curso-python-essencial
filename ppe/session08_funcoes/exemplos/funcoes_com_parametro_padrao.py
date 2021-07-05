"""
Funções com parâmetros padrão (Default Parameters)
 - Funções onde a passagem de parâmetros seja opcional;
"""


# Função onde a passagem de parâmetro é obrigatória
def soma(num1, num2):
    return num1 + num2


print(f'Soma de 4 + 3 = {soma(4, 3)}')
"""
ERRO! -> TypeError
print(f'Soma de 4 = {soma(4)}') 
print(f'Soma = {soma()}')

Ambos os valores, num1 e num2, são obrigatórios caso não seja passado valores para eles
a chamada para a função dará erro por estar faltando argumentos.
"""


print("--------------------------------------------------")


# Ao definir uma função, se colocarmos um valor nos parâmetros, estamos dizendo
# que esse valor é o padrão e caso não seja passado nenhum parâmetro,
# ele será usado para no processamento.
def exponencial(numero, potencia=2):
    return numero ** potencia


print(f'2 elevado a 3 é: {exponencial(2, 3)}')
print(f'3 elevado a 2 é: = {exponencial(2, 3)}')

# Por padão, quando não houver potência, elevar ao quadrado
print(f'3 elevado a 2 (padrão) é = {exponencial(3)}')
print(f'3 elevado a 5 é: = {exponencial(3, 5)}')

# OBS 1.: Se o usuário passar somente 1 argumento, este será atribuído ao parâmetro número
# e será calculado o quadrado deste número.

# OBS 2.: Se o usuário passar os 2 argumentos, o primeiro será atribuído ao parâmetro número
# e o segundo ao parâmetro potência e então será calculada essa potência.

"""
Os parâmetros com valores default DEVEM sempre estar ao final da declaração.

# ERRO! -> non-default parameter follows default parameter
def teste(num=2, potencia):
    return num ** potencia
"""

print("--------------------------------------------------")


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(f'Chamada a função mostra_informacao(): {mostra_informacao()}')
print(f'Chamada a função mostra_informacao(instrutor=True): {mostra_informacao(instrutor=True)}')
print(f'Chamada a função mostra_informacao(True): {mostra_informacao(True)}')
print(f'Chamada a função mostra_informacao("Ozzy"): {mostra_informacao("Ozzy")}')
print(f'Chamada a função mostra_informacao(nome="Stephany"): {mostra_informacao(nome="Stephany")}')

"""
Por quê utilizar parâmetros com valor default?
 - Nos permite ser mais flexíveis nas funções;
 - Evita erros com parâmetros incorretos;
 - Nos permite trabalhar com exemplos mais legíveis de código;
"""

print("--------------------------------------------------")
# Passando uma função como parâmetro


def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


print(f'mat(2, 3) = {mat(2, 3)}')
print(f'mat(2, 2, subtracao) = {mat(2, 2, subtracao)}')

print("--------------------------------------------------")
# Escopo - Evitar problemas e confusões

instrutor = 'Geek'  # Variável global


def diz_oi():
    instrutor = 'Python'  # Variável local
    return f'Oi {instrutor}'


print(f'executando a função diz_oi: {diz_oi()}')

# OBS.: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferencia.

print("--------------------------------------------------")
# ATENÇÃO com variáveis globais (Se puder evitar, evite!!)

total = 0


def incremento():
    # total = total + 1  # UnboundLocal -> A variável local está sendo usada, sem ter sido inicializada dentro da função

    # Para corrigir o erro acima
    global total  # É preciso informar ao Python que queremos usar a variável global dentro da função
    total = total + 1

    return total


print(f'executando a função incremento(): {incremento()}')
print(f'executando a função incremento(): {incremento()}')
print(f'executando a função incremento(): {incremento()}')

print("--------------------------------------------------")
# Podemos ter funções que são declaradas dentro de funções e há uma forma especial de escopo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador  # indica que a variável não é local, porém também não é global
        contador = contador + 1
        return contador
    return dentro()


print(f'executando a função fora(): {fora()}')
print(f'executando a função fora(): {fora()}')
print(f'executando a função fora(): {fora()}')

# print(f'executando a função dentro(): {dentro()}')  # NameError
# a função dentro só é conhecida no escopo da função fora
