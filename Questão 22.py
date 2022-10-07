# 22) Desenvolva um programa para registrar o levantamento dos testes de 200 mouses. O programa deverá receber um número indeterminado de entradas, cada uma contendo um número de identificação do mouse e o tipo de defeito: a) Necessita da esfera; b) Necessita de limpeza; c) Necessita troca do cabo ou conector; d) Quebrado ou inutilizado. Uma identificação igual a 0 encerra o programa.
mouses = [0, 0, 0, 0]
estado = ['Necessita da Esfera', 'Necessita de Limpeza',
          'Necessita troca de cabo ou conector', 'Quebrado ou Inutilizado']
x, cont = 0, 0

def vazio(msg):
    ok = False
    valor = 0
    while True:
        v = str(input(msg))
        if v.isnumeric():
            valor = int(v)
            ok = True
        else:
            print('Digite um valor válido!')
        if ok:
            break
    return valor


print('Informe o estado do mouse de acordo com as opções.\n')
print('1 - Necessita da Esfera. 2 - Necessita de Limpeza, 3 - Necessita troca de cabo ou conector. 4 - Quebrado ou Inutilizado\n')
while x == 0:
    mouse = vazio('Estado do Mouse: ')

    if mouse > 6:
        print('Valor inválido!')
        break
    elif mouse > 0 and mouse < 5:
        cont += 1
        mouses[mouse - 1] += 1
    else:
        if mouse == 0 and cont == 0:
            print('Fim da Votação!')
            break
        else:
            print('\nQuantidade de mouses: {}'.format(cont))
            print('\n{:<40} {:<15} {:<10}'.format(
                'Situação', 'Quantidade', 'Percentual'), end='')

            for g in range(len(mouses)):
                porc = (mouses[g] / cont) * 100
                print('\n{} - {:<40} {:<15} {:<10}'.format(g + 1, estado[g], mouses[g], '%.2f' % porc, end=''))
            print('\n')    
            break
