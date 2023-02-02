from random import randint
print('Irei escolher um número de 0 a 5 tente adivinhar')
random = randint(0, 5)
usuario = int(input('Escolha um número entre 0 a 5: '))

if random == usuario:
    print('Parabéns, você acertou!')
else:
    print(f'Sinto muito, o número era {random}')