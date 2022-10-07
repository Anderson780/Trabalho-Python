#O vendedor recebe R$ 200 por semana mais um 9% de suas vendas brutas daquela semana. Escreva um programa que determine quantos vendedores receberam salários de 200 a 299, 300 a 399... 1000 em diante.
# Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer ifs aninhados.

valores = [0, 0, 0, 0, 0, 0, 0, 0, 0]
x, z = 0, 0

for x in range(8):
    while z != -1:
        comissao = int(input('Digite a sua comissão: '))
        if comissao == -1:
            z = -1
        else:
            salario = 200 + ((9 / 100) * comissao)
            print('Seu salário foi de R$ %.2f' % salario,'\n')
            if salario > 1000:
                valores[8] += 1
            else:
                valores[int(salario / 100) - 2] += 1
                
    print('R$ %d00 - R$%d99: %d' % (x + 2, x + 2, valores[x]))
    
print('R$ 1000 em diante: %d' % valores[8])