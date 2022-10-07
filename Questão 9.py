# Faça um programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
nm = []
sm = 0

for x in range(10):
    z = int(input('Digite um número: '))
    quad = z * z
    sm += quad
    nm.append(quad)

print('Os quadrados dos números:', *nm)
print('A soma dos quadrados dos números:{}'.format(sm))