# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
num1, num2, num3, num4 = [], [], [], []
x = 0

while x < 10:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    n3 = int(input('Digite um número: '))

    num1.append(n1)
    num2.append(n2)
    num3.append(n3)

    if n1 % 2 == 0:
        num4.append(n1)
    elif n2 % 2 == 1:
        num4.append(n2)
    elif n3 % 2 == 1 or n3 % 2 == 0:
        num4.append(n3)
    x += 1

print('Os números do primeiro vetor: ', *num1)
print('Os números do segundo vetor: ', *num2)
print('Os números do terceiro vetor: ', *num3)
print('Os números intercalados: ', *num4)