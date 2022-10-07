# 24) Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor. Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores (1 - 6) e uma função para gerar números aleatórios, simulando os lançamentos dos dados.
import random

dados = [0,0,0,0,0,0]
x = 0

while x < 100:
    y = random.randrange(0,6)
    dados[y] += 1
    x += 1

for z in range(6):
    print('Lado {}: {} vezes'.format(z + 1, dados[z]))
        