# Faça um programa que leia um vetor de 5 números inteiros e mostre-os.
num = []
x = 0

while x < 5:
  z = int(input('Digite um número: '))
  num.append(z)
  x += 1

print(num)