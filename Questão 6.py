# Faça um programa que peça as quatros notas de 10 alunos, calcule e armazene num vetor a média de cada aluno e imprima o número de alunos com média maior ou igual a 7.0.
medias = []
x, ap = 0, 0

while x < 10:
    z, stn = 0, 0

    while z < 4:
        notas = float(input('Digite a nota: '))
        stn += notas
        z += 1

    if (stn / 4) >= 7:
        ap += 1
    medias.append(stn / 4)
    print('Média do aluno: ', stn / 4)
    print('Próximo aluno!\n')
    x += 1

print('Números de alunos com média maior ou igual a 7: {}'.format(ap), 'aluno(s).\n')