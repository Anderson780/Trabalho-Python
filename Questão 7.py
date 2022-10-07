# Faça um programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
num = []
soma, multi = 0, 1

for x in range(5):
    z = int(input('Digite um número: '))
    soma += z
    multi = multi * z
    num.append(z)

print('\nOs números somados: {}'.format(soma))
print('Os números multiplicados: {}'.format(multi))
print('Todos os números: ', *num)