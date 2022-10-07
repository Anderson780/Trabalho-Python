# Faça um programa para saber qual o melhor Sistema Operacional para uso em servidores? As possíveis respostas são: 1- Windows Server, 2- Unix, 3- Linux, 4- Netware, 5- Mac OS, 6- Outro. O programa deve ler o resultado da enquete e informe ao final o resultado da mesma. Ao ser informado 0, o programa encerra. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenadas num vetor. Após os dados terem sido completamente informados, o programa deverá calcular o percentual de cada um dos concorrentes e informar o vencedor da enquete.
votos = [0, 0, 0, 0, 0, 0]
so = ['Windows Server','Unix', 'Linux', 'Netware', 'MacOs', 'Outros']
x, cont, mv = 0, 0, 0

def vazio(msg):
    ok = False
    valor = 0
    while True:
        v = str(input(msg))
        if v.isnumeric():
            valor = int(v)
            ok = True
        else:
            print('Digite um número válido!')
        if ok:
            break
    return valor

print('Enquete: Qual o melhor Sistema Operacional para uso em servidores?')
print('Digite: 1 - Windows Server, 2 - Unix, 3 - Linux, 4 - Netware, 5 - Mac OS, 6 - Outro')

while x != -1:
    v = vazio('Digite seu voto: ')

    if v > 6:
        print('Valor inválido!')
        break
    elif v > 0 and v <= 6:
        votos[v - 1] += 1
        cont += 1
   
    else:
        if v == 0 and cont == 0:
            print('Fim da Votação!')
            break
        else:
            print('\nResultado da Votação!')
            print('Foram computados {} votos'.format(cont), '\n')
            print("{:<20} {:<7} {:<10}".format('Sistema Operacional', 'Votos', '%'), end="")
            print('\n--------------------------------')

            for g in range(6):
                z = votos[g]
                if z > 0:
                    porc = float(z / cont) * 100
                    print("\n{:<20} {:<7}".format(so[g], z), end='')
                    print('%.2f' % porc )
                if z > mv:
                    mv = z
                    jmv = g + 1
                    porcm = float(z / cont) * 100

        print('\nO Sistema Operacional mais votado foi o {}, com {} votos, correspondendo a {:.2f} % do total dos votos.'.format(so[jmv],mv, porcm))
        break