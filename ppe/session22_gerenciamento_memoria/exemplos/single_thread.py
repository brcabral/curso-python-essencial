import time

CONTADOR = 50_000_000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


inicio = time.time()
contagem_regressiva(CONTADOR)
fim = time.time()

print(f'Tempo em segundos single thread: {fim - inicio}')

# Tempo em segundos single thread: 3.4991254806518555
# Tempo em segundos single thread: 2.9900014400482178
# Tempo em segundos single thread: 2.997483730316162
