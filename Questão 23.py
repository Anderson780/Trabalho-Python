# 23) Crie um programa que gere um relatório, chamado 'relatório.txt. O arquivo de entrada só deve ser lido uma vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão do espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual também deverá ser feito através de uma função.
usuarios, numeros = [], []
vt, total = 0, 0

def mb(valores):
    for x in range(2):
        valores = valores / 1024
    return valores

def porc(valores,total):
    pc = ((valores / total) * 100)
    return pc

with open('usuarios.txt', 'r') as Arquivo:
    for line in Arquivo:
        x = (line[0:14])
        usuarios.append(x.strip())
        x = (line[14:])
        x = int(x.strip())
        numeros.append(x)
        vt += x
vt = mb(vt)

print('ACME INC.  Uso do espaço em disco pelos usuários')

print('--------------------------------------------------')
print ("{:<5} {:<15} {:<20} {:<15}".format("N.","Usuário","Espaço utilizado", "% do uso"))

for x in range(len(usuarios)):
    u = mb(numeros[x])
    print('{:<5} {:<15} {:<20} {:<15}'.format((x + 1), usuarios[x], ('%.2f MB' % u), ('%.2f%%' %porc(u, vt))))
print('\nEspaço total ocupado: {:.2f} MB'.format(vt))
print('Espaço médio ocupado: {:.2f} MB'.format(vt / len(usuarios)))