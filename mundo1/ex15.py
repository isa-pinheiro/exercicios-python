d = int(input('Insira quantos dias o carro foi alugado: '))
km = float(input('Insira a quantidade de quilômetros rodados: '))
v = 60* d + 0.15 * km
print('O total a pagar é {:.2f}'.format(v))