lado = []

for i in range(3):
    lado.append(float(input(f'Insira o {(i + 1)}° lado do triângulo: ')))
    
if lado[0] + lado[1] > lado[2] and lado[1] + lado[2] > lado[0] and lado[0] + lado[2] > lado[1]:
    print('É possível formar esse triângulo')
else:
    print('Não é possível formar esse triângulo')