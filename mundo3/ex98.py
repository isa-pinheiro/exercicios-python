def contagem(a, b, i):
    print(f'contador de {a} a {b} contando de {i} em {i}')
    if a < b:
        for i in range(a, b+i, i):
            print(i, end=' ')
    else:
        for i in range(a, b-i, -i):
            print(i, end=' ')
    print('Fim.')
    
contagem(1, 10, 1)
contagem(10, 0, 2)