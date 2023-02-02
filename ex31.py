dis = float(input('Insira a distância percorrida em km: '))

if dis <= 200:
    preco = 0.5 * dis
    print(f'O valor ficou {preco}')
else:
    preco = 0.45 * dis
    print(f'O valor ficou {preco}')