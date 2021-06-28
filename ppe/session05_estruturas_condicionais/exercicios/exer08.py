"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas.
Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0,
onde caso a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa termina.
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
    media = (nota1 + nota2) / 2
    print(f"A média das notas é {media}")
else:
    print("Uma ou mais nota(s) possue(m) valor(es) inválido(s).")
