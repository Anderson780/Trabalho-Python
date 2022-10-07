# Faça um programa que leia um vetor de 10 números reais e mostre na ordem inversa.
num = []
x = 0

while x < 10:
    z = int(input('Digite um número: '))
    num.append(z)
    x += 1

num.reverse()
print(num)