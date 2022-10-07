# Faça um programa de votação do melhor jogador de um jogo. Onde o número de jogador igual a 0, indica que a votação foi encerrada. O programa deverá exibir: a) O total de votos computados; b) Os números e respectivos votos de todos os jogadores que receberam votos; c) O percentual de votos de cada um destes jogadores; d) O número do jogador escolhido como melhor da partida, juntamente com o número de votos dados a ele.
votos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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

while x != -1:
    v = vazio('Enquete: Quem foi o melhor jogador? ')

    if v > 0 and v < 23:
        votos[v - 1] += 1
        cont += 1
    else:
        if v == 0 and cont == 0:
            print('Fim da Votação!')
            break
        else:
            with open("Resultado.txt", "w", encoding="UTF-8") as Arquivo:
                print('\nResultado da Votação!', file=Arquivo)
                print('Foram computados {} votos'.format(cont), '\n', file=Arquivo)
                print("{:<10} {:<9} {:<10}".format('Jogador', 'Votos', '%'), end="", file=Arquivo)

                for g in range(23):
                    z = votos[g]
                    if z > 0:
                        porc = float(z / cont) * 100
                        print("\n{:<10} {:<10}".format(g + 1, z), end='', file=Arquivo)
                        print('%.2f' % porc , file=Arquivo)
                    if z > mv:
                        mv = z
                        jmv = g + 1
                        porcm = float(mv / cont) * 100

                print('\nO melhor jogador foi o número {}, com {} votos, correspondendo a {:.2f} % do total dos votos.'.format(jmv, mv, porcm), file=Arquivo)
            Arquivo.close()
            break