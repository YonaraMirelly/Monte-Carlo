import itertools

# Definir os valores das cartas do baralho
baralho = [1] * 4 + list(range(2, 11)) * 4 + [10] * 4 * 3  # Ases, cartas numeradas e figuras

# Total de combinações possíveis
total_combinacoes = len(list(itertools.combinations(baralho, 3)))

# Contador de combinações que somam 21
contador_soma_21 = 0

# Contar todas as combinações de 3 cartas que somam 21
for combinacao in itertools.combinations(baralho, 3):
    if sum(combinacao) == 21:
        contador_soma_21 += 1

# Calcular a probabilidade
probabilidade_exata = contador_soma_21 / total_combinacoes

print(f"Número total de combinações: {total_combinacoes}")
print(f"Número de combinações que somam 21: {contador_soma_21}")
print(f"Probabilidade exata de soma igual a 21: {probabilidade_exata:.6f}")
print(f'porcentagem -> {probabilidade_exata*100:.2}%')
