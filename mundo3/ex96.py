def area(lar, comp):
    a = lar * comp
    print(f'A área de um terreno {lar} por {comp} é {a}')
    
print('-' * 30)
print('controle de terreno')
l = float(input('Largura do terreno (m): '))
c = float(input('Comprimento do terreno (m): '))
area(l,c)