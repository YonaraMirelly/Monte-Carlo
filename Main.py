import random as rd
import time
'''
SIMULACAO DE MONTE CARLO

Alunos:
Igor Barros Lins de Queiroz
Yonara Mirelly Araújo da Silva

PROBLEMA 8: Jogando Baralho

Qual a probabilidade de que a
soma de 3 cartas de um baralho
seja 21?

'''
'''
PASSO 1: Gerar dados
'''
inicio = time.time()
def cria_baralho(): #CRIA O BARALHO COM 52 CARTAS
    return ['A',2,3,4,5,6,7,8,9,10,'J','K','Q']*4 #CADA UM DOS 4 NAIPES TEM 13 CARTAS
    
def retirar_cartas(baralho): #RETIRA 3 CARTAS ALEATÓRIAS DO BARALHO
    cartas_retiradas = rd.sample(baralho, 3) 
    return cartas_retiradas
'''
PASSO 2: Testar dados
'''
def soma(cartas): #SOMA AS CARTAS 3 CARTAS OBTIDAS
    soma_cartas = 0
    for carta in cartas:
        if carta == 'A':
            valor = 1
        elif carta in ['Q','J','K']:
            valor = 10
        else:
            valor = carta
            
        soma_cartas += valor
        
    return soma_cartas

def teste(cartas): #VÊ SE A SOMA DAS CARTAS É 21
    if soma(cartas) == 21:
        return True
    else:
        return False

'''
PASSO 3: Uma simulação

Parâmetros:
qtd_jogadas = Quantas vezes serão retiradas 3 cartas do baralho
'''

def simulacao(qtd_jogadas): #UMA SIMULAÇÃO EM QUE UM JOGADOR RECEBE 3 CARTAS N VEZES
    #contar a quantidade de vezes que obtemos soma = 21
    contador = 0
    baralho = cria_baralho()

    for _ in range(qtd_jogadas):
        cartas = retirar_cartas(baralho) #RETIRA 3 CARTAS E ARMAZENA

        if teste(cartas): #SE A SOMA DAS 3 CARTAS RETIRADAS NA RODADA FOR 21, CONTADOR AUMENTA
            contador += 1

    return contador/qtd_jogadas

'''
PASSO 4: Simulação completa

Parâmetros:
qtd_jogadas = Quantas vezes serão retiradas 3 cartas do baralho
simulacoes = quantas simulacoes serão feitas com a quantidade de jogadas
'''

def simulacao_completa(qtd_jogadas, simulacoes): #SIMULAÇÃO COMPLETA, EM QUE O JOGADOR
    # Soma quantas vezes o número 21 foi obtido durante todas as jogadas, para fazer a media
    soma = 0

    for _ in range(simulacoes):
        soma += simulacao(qtd_jogadas)

    # Retorna média das simulacoes
    return soma/simulacoes
fim= time.time()
qtd_jogadas = 1000
simulacoes = 1000
probabilidade = simulacao_completa(qtd_jogadas, simulacoes)
print(f"Probabilidade: {probabilidade:.4f} -> {probabilidade*100:.1f}%")
print(f'Tempo de execução: {inicio-fim}')


