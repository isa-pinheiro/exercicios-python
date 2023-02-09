numeros = []
for i in range(5):
    numeros.append(int(input(f'insira o numero da posiçao {i}: ')))
    
print(f'as posições do maior numero {max(numeros)} é ', end='')
for pos, num in enumerate(numeros):
    if num == max(numeros):
        print(f'{pos}', end='... ')
        
print(f'\nas posições do menor numero {min(numeros)} é ', end='')
for pos, num in enumerate(numeros):
    if num == min(numeros):
        print(f'{pos}', end='... ')
        

print(f'voce digitou os numeros {numeros}')
