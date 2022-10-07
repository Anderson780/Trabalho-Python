# Faça um programa que peça a idade e a altura de 5 pessoas, armazenando em vetores e imprima a idade e a altura na ordem inversa a ordem lida.
idade, altura  = [], []
x = 0

while x < 5:
    idd = int(input('Digite a sua idade: '))
    alt = float(input('Digite sua altura: '))
    idade.append(idd)
    altura.append(alt)
    x += 1

print('As idades na ordem inversa:', idade[:: -1])
print('As alturas na ordem inversa:', altura[:: -1])
