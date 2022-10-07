# Faça um programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
num1, num2, num3 = [], [], []
x = 0

while x < 10:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))

    num1.append(n1)
    num2.append(n2)

    if x % 2 == 0:
        num3.append(n1)
    else:
        num3.append(n2)
    x += 1

print('Os números do primeiro vetor: ', *num1)
print('Os números do segundo vetor: ', *num2)
print('Os números intercalados: ', *num3)
