# Faça um programa que leia 4 notas, mostre as notas e a média na tela.
notas = []
media = 0
x = 0

while x < 4:
    z = float(input('Digite a nota: '))
    notas.append(z)
    media += z
    x += 1

print('As notas: {}'.format(*notas))
print('A média: {}'.format(media/4))
