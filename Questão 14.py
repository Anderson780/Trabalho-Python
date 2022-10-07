# Faça 5 perguntas para uma pessoa sobre um crime. "Telefonou para a vítima?"; "Esteve no local do crime?"; "Mora perto da vítima?"; "Devia para a vítima?"; "Já trabalhou com a vítima?". Se a resposta for sim a 2 questões, ela é "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, "Inocente".
sim, nao = [],[]

print('Responda as perguntas com sinceridade!')

x = input('Telefonou para a vítima? ')

if x == 'n' or x == 'N' or x == 'Nao' or x == 'Não' or x == 'NAO' or x == 'NÃO':
    nao.append(x)
elif x == 's' or x == 'S' or x == 'Sim' or x == 'SIM' or x == 'sim':
    sim.append(x)
else:
    print('Fale a verdade!')

x = input('Esteve no local do crime? ')

if x == 'n' or x == 'N' or x == 'Nao' or x == 'Não' or x == 'NAO' or x == 'NÃO':
    nao.append(x)
elif x == 's' or x == 'S' or x == 'Sim' or x == 'SIM' or x == 'sim':
    sim.append(x)
else:
    print('Fale a verdade!')

x = input('Mora perto da vítima? ')

if x == 'n' or x == 'N' or x == 'Nao' or x == 'Não' or x == 'NAO' or x == 'NÃO':
    nao.append(x)
elif x == 's' or x == 'S' or x == 'Sim' or x == 'SIM' or x == 'sim':
    sim.append(x)
else:
    print('Fale a verdade!')

x = input('Devia para a vítima? ')

if x == 'n' or x == 'N' or x == 'Nao' or x == 'Não' or x == 'NAO' or x == 'NÃO':
    nao.append(x)
elif x == 's' or x == 'S' or x == 'Sim' or x == 'SIM' or x == 'sim':
    sim.append(x)
else:
    print('Fale a verdade!')


x = input('Já trabalhou com a vítima? ')

if x == 'n' or x == 'N' or x == 'Nao' or x == 'Não' or x == 'NAO' or x == 'NÃO':
    nao.append(x)
elif x == 's' or x == 'S' or x == 'Sim' or x == 'SIM' or x == 'sim':
    sim.append(x)
else:
    print('Fale a verdade!')

if len(sim) == 2:
    print('Você é suspeito!')
elif len(sim) > 2 and len(sim) <= 4:
    print('Você é cúmplice!')
elif len(sim) == 5:
    print('Você é culpado!')
else:
    print('Você é inocente!')
