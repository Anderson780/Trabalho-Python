# Faça um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos, e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome.

saltos, nomes = [], []
x, soma = 1, 0

while x != 0:
    nome = input('Digite seu nome: ')
    if nome != '':
        nomes.append(nome)
        for y in range(5):
            salt = float(input('Informe as distâncias dos saltos: '))
            soma += salt
            saltos.append(salt)

        print('\nAtleta: {}'.format(*nomes))
        for y in range(5):
            print(y + 1, '° salto:', saltos[y], 'm')
        print('Média dos saltos: {}'.format(soma / 5), 'm\n')

    else:
        if len(nomes) > 0:
            print('\nResultado Final:')
            print('Atleta: {}'.format(*nomes))
            print('Saltos: ', end="")
            for y in range(5):
                if y != 4:
                    print('%.2f' % saltos[y], end=' - ')
                else:
                    print('%.2f' % saltos[y], end=' ')
            print('\nMédia dos saltos: {}'.format(soma / 5), 'm\n')
            print('Fim')
            break
        else:
            print('Fim!')
            break