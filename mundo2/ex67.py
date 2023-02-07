n = 0
while True:
    n = int(input('insira um número para ver a tabuada: '))
    if n < 0:
        break
    print('-' * 10)
    for i in range (1,11):
        print(f'{n} x {i} = {n*i}')
    print('-' * 10)