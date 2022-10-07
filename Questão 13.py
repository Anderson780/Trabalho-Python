# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e o mes.
temp, mes1= [], []
x, z, mtemp = 0, 0, 0

while x < 12:
    mes = (input('Digite o mês: '))
    tprt = float(input('Digite a média de temperatura: '))
    mtemp += tprt
    temp.append(tprt)
    mes1.append(mes)
    x += 1

media = float(mtemp / 12)
print('\nMédia anual de temperatura: {%.2f}'.format(media))
print('Os meses com temperaturas acima da média foram:')

c = 0

while z < 12:
    if temp[z] > media:
        mes1.sort()
        c += 1
        print(c, '-', mes1[z])
    z += 1
