import random
import numpy as np


def probabilidade(n):
 
    baralho = [1] * 4 + list(range(2, 11)) * 4 + [10] * 4 * 3  
    contador = 0
    print(baralho)
    s=0
    for i in baralho:
        s+=1
    print(f'total de cartas : ', s)

    for _ in range(n):
        cartas_retiradas = random.sample(baralho, 3)
        if sum(cartas_retiradas) == 21:
            contador += 1

    return round(contador / n, 6)

valores_simulacoes = [100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]

for n in valores_simulacoes:
    prob = probabilidade(n)
    print(f'n = {n} | Probabilidade estimada de soma igual a 21: {prob*100:2f}%')
