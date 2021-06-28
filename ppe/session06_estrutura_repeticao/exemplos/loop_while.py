"""
Loop while
O bloco do while será repetido enquanto a expressão booleana for verdadeira
Em um loop while, é importante que cuidemos do critéria de parada para não causar um loop infinito

while expressao_boleana:
    # execucao_do_loop
"""

numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1

print("--------------------------------------------------")

resposta = ""

while resposta != "sim":
    resposta = input("Já acabou? ")

print("--------------------------------------------------")
