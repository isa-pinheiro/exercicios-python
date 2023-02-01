n = int(input('Insira um número para ver a tabuada: '))

for i in range(10):
    print('{} x {} = {}'.format(n, i+1, ((i+1)*n)))
