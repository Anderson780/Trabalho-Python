# Faça um programa que leia um vetor de 10 caracteres, que diga e imprima as consoantes.
lt = []
x = 0

while x < 10:
    z = input('Digite as letras: ')
    if z != 'a' and z != 'e' and z != 'i' and z != 'o' and z != 'u':
        lt.append(z)
    x += 1

print('Número de consoantes: {}'.format(len(lt)))
print('Consoantes:', *lt)