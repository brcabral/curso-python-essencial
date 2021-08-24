import time
from threading import Thread

CONTADOR = 50_000_000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


t1 = Thread(target=contagem_regressiva, args=(CONTADOR//2,))
t2 = Thread(target=contagem_regressiva, args=(CONTADOR//2,))

inicio = time.time()
t1.start()
t2.start()
t1.join()
t1.join()
fim = time.time()

print(f'Tempo em segundos multi thread: {fim - inicio}')

# Tempo em segundos multi thread: 4.572606563568115
# Tempo em segundos multi thread: 4.715313196182251
# Tempo em segundos multi thread: 4.718400001525879
