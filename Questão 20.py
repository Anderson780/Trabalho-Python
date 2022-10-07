# 20) As Organizações Tabajara resolveram dar um abono aos seus colaboradores; Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro. O piso do abono será de 100 reai. Seu programa deverá permitir a digitação do salário de um número indefinido de salários. Um valor de salário igual a 0 encerra a digitação. Ao final do programa deverá apresentar: a) O salário de cada funcionário, juntamente com o valor do abono; b) O número total de funcionários processados; c) O valor total a ser gasto com o pagamento do abono; d) O número de funcionários que receberá o valor mínimo de 100 reais; f) O maior valor pago com o abono.
salario, abono = [], []
x, at = 0, 0

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


while x == 0:
    v = vazio('Digite seu salário: ')

    if v > 0:
        salario.append(v)
        abon = v * (20/100)

        if abon < 100:
            abon = 100
            at += abon
            abono.append(abon)
        else:
            at += abon
            abono.append(abon)

    elif v == 0 and len(salario) == 0:
        print('Fim da Votação!')
        break
    else:
        print("{:<16} {:<1}".format('\nSalário', 'Abono'), end="")
        print('\n----------------------------')

        for g in range(len(salario)):
            print("\n{:<15} {:<13}".format("R$ %.2f" %
                  salario[g], "R$ %.2f" % abono[g]), end='')
        x = 1

print('\n\nForam processados {} colaboradores'.format(len(salario)))
print('Total gasto com abonos: R$ {}'.format(at))
print('Valor mínimo pago a {} colaborador(es)'.format(abono.count(100)))
print('Maior valor de abono pago: R$ {}'.format(max(abono)))
