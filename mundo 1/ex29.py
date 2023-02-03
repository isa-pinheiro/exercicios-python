vel = float(input('Insira a velocidade do carro: '))

if vel <= 80:
    print('Pode seguir')
else:
    multa = (vel - 80) * 7
    print(f'Você ultrapassou a velocidade, sua multa será {multa}')