# De acordo com a idade e altura de 30 alunos, faça um programa que determine quantos alunos com mais de 13 anos possuem altura inferior a média de altura desses alunos.
idade, altura = [], []
x, z, media = 0, 0, 0

while x < 30:
    idd = int(input('Digite a sua idade: '))
    alt = float(input('Digite sua altura: '))
    media += alt
    idade.append(idd)
    altura.append(alt)
    x += 1

malt = float(media / len(altura))

print('\nA média de altura dos alunos: {%.2f}'.format(malt))

while z < len(altura):
    if idade[z] > 13 and altura[z] <= malt:
        print('Aluno com altura menor que a média!')
    else:
        print('Aluno com altura maior que a média!')
    z += 1