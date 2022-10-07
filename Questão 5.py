# Faça um programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor Par e os números Impares no vetor impar. Imprima três valores.
vt1, vt2, vt3 = [], [], []
x = 0

while x < 20:
    z = int(input('Digite os números: '))
    vt1.append(z)
    if z % 2 == 0:
        vt2.append(z)
    else:
        vt3.append(z)
    x += 1

print('Todos os números: ', *vt1)
print('Todos os números pares: ', *vt2)
print('Todos os números impares: ', *vt3)