matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
somap = 0
soma2 = 0
mai = 0
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'insira o [{i},{j}]: '))
        if matriz[i][j] % 2 == 0:
            somap += matriz[i][j]
        if j == 2:
            soma2 += matriz[i][j]
        if i == 1 and j == 0:
            mai = matriz[i][j]
        if i == 1:
            if matriz[i][j] > mai:
                mai = matriz[i][j]
            
            
            

print('=' * 20)

for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end=' ')
    print( )
    
print('=' * 20)

print(f'soma dos pares {somap}')
print(f'soma dos digitos na terceira coluna {soma2}')
print(f'o maior na linha dois {mai}')