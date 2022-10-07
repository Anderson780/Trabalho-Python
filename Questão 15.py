# Faça um programa que leia vários notas, encerrando quando for informado um valor igual a -1. Funções do programa: Exiba todos os valores na ordem que forem informados, um do lado do outro; Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro; Calcule e mostre a soma dos valores; Calcule e mostre a média dos valores; Calcule e mostre a quantidade de valores acima da média calculada; Calcule e mostre a quantidade de valores abaixo de sete; Encerre o programa com uma mensagem.

import pandas as pd

notas = []
x, z, n1, n2, soma = 0, 0, 0, 0, 0

while x == 0:
    num = int(input('Digite uma nota: '))
    if num == -1:
        x += 1
        print('Fim!')
    else:
        notas.append(num)
        soma += num

media = soma / len(notas)

while z < len(notas):
    if notas[z] > media:
        n1 += 1
    z += 1

z = 0

while z < len(notas):
    if notas[z] < 7:
        n2 += 1
    z += 1

df = pd.DataFrame(notas[:: -1], columns=['Notas'])

print('\nTodas as notas:', *notas)
print('Todas as notas em ordem inversa:', df)
print('\nA soma de todas as notas: {}'.format(soma))
print('A média de todas as notas: {:.2f}'.format(media))
print('Números de notas acima da média: {}'.format(n1))
print('Números de notas menor que sete: {}'.format(n2))