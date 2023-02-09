fanchantorder = ('namjoon', 1, 'seokjin', 2, 'yoongi', 3, 'hobi', 4, 'jimin', 5, 'tae', 6, 'jk',7)

for i in range(0, len(fanchantorder)):
    if i % 2 == 0:
        print(f'{fanchantorder[i]}', end=' ')
    else:
        print(f'é o {fanchantorder[i]}º')