"""
Novas funções matemática e estatística
"""

import math
import statistics

""" *** Funções matemáticas *** """
# math.prod -> retorna o produto de um container numérico
nuns_v1 = [2, 3, 6, 8]
nuns_v2 = (2, 3, 6, 8)
nuns_v3 = {2, 3, 6, 8}

print(f'{math.prod(nuns_v1) = }')
print(f'{math.prod(nuns_v2) = }')
print(f'{math.prod(nuns_v3) = }')

print("--------------------------------------------------")

# math.isqrt -> retorna o valor inteiro de uma raiz quadrada de um número
print(f'{math.isqrt(9) = }')
print(f'{math.sqrt(9) = }')
print(f'{math.isqrt(17) = }')
print(f'{math.sqrt(17) = }')

print("--------------------------------------------------")

# math.dist -> retorna a distância euclidiana entre dois pontos (2D ou 3D)
# Pontos 2D
p2d1 = [12, 50]
p2d2 = (6, 7)

# Pontos 3D
p3d1 = (12, 50, 40)
p3d2 = [6, 7, 13]

print(f'{math.dist(p2d1, p2d2) = }')
print(f'{math.dist(p3d1, p3d2) = }')

print("--------------------------------------------------")

# math.hypot -> retorna a hipotenusa ou norma Euclidiana
# Pontos 2D
p2d1 = [12, 50]

# Pontos 3D
p3d1 = (12, 50, 40)

print(f'{math.hypot(*p2d1) = }')
print(f'{math.hypot(*p3d1) = }')

print("--------------------------------------------------")

""" *** Funções estatísticas *** """
# statistics.fmean -> calcula a média de números reais
valores_reais = [1.45, 6.789, 3.45, 89.98765]
valores_inteiros = [1, 6, 3, 89]

print(f'{statistics.fmean(valores_reais) = }')
print(f'{statistics.fmean(valores_inteiros) = }')

print("--------------------------------------------------")

# statistics.geometric_mean -> calcula a média geométrica de números reais
valores_reais = [1.45, 6.789, 3.45, 89.98765]
valores_inteiros = [1, 6, 3, 89]

print(f'{statistics.geometric_mean(valores_reais) = }')
print(f'{statistics.geometric_mean(valores_inteiros) = }')

print("--------------------------------------------------")

# statistics.multimode -> retorna o valor mais frequente em uma sequência
seq1 = 'Geek University'
seq2 = [3, 5, 3, 8, 7, 9, 5, 3]
seq3 = [1, 2, 3, 1, 2, 3, 4, 5, 6]

print(f'{statistics.multimode(seq1) = }')
print(f'{statistics.multimode(seq2) = }')
print(f'{statistics.multimode(seq3) = }')
