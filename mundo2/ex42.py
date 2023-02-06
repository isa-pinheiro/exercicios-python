lado = []

for i in range(3):
    lado.append(float(input(f'Insira o {(i + 1)}° lado do triângulo: ')))

equilatero = (lado [0] == lado[1] == lado[2])
escaleno = (lado [0] != lado[1] != lado[2] != lado[0])

if lado[0] + lado[1] > lado[2] and lado[1] + lado[2] > lado[0] and lado[0] + lado[2] > lado[1]:
    if equilatero:
        print('O triângulo é equilátero')
    elif escaleno:
        print('O triângulo é escaleno')
    else: 
        print('O triângulo é isoceles')
else:
    print('Não é possível formar esse triângulo')