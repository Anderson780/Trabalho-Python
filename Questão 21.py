# 21) Faça um progrma que carregue uma lista com os modelos de cinco carros. Carregue uma outra lista com o consumo desses carros, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre: a) O modelo do carro mais econômico; b) Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 km e quanto isso custará, considerando que a gasolina custe R$ 2,25 o litro.
carros, kpl = [], []
x, ce = 0, 0

while x < 5:
   print('Veículo {}'.format(x + 1))
   carro = input('Carro: ')
   lpkm = float(input('Km por litro: '))
   carros.append(carro)
   kpl.append(lpkm)
   x += 1

print('\nRelatório Final')

for g in range(5):
    dist = 1000 / kpl[g]
    vt = dist * 2.25
    print("\n{} - {:<10} {:<10} {:<18} {:<18} ".format(g + 1, carros[g], kpl[g], "%.2f litros" % dist, "R$ %.2f" % vt), end='')
    if kpl[g] > ce:
        ce = kpl[g]
        pc = kpl.index(ce)
print('\n\nO menor consumo é do(a) {}.'.format(carros[pc]))

