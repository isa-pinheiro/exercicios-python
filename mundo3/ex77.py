
bts = ('namjoon', 'seokjin', 'yoongi', 'hobi', 'jimin', 'tae', 'jk')

for nome in bts:
    print(f'na palavra {nome.upper()} tem as vogais: ', end='')
    for letra in nome:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
    print('\n')