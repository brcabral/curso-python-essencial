import time
from multiprocessing import Pool

CONTADOR = 50_000_000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


pool = Pool(processes=2)
inicio = time.time()

p1 = pool.apply_async(contagem_regressiva, [CONTADOR//2])
p2 = pool.apply_async(contagem_regressiva, [CONTADOR//2])

pool.close()
pool.join()

fim = time.time()

print(f'Tempo em segundos multi processing: {fim - inicio}')

# Tempo em segundos multi processing: 1.834331750869751
# Tempo em segundos multi processing: 1.6506974697113037
# Tempo em segundos multi processing: 1.6680915355682373
