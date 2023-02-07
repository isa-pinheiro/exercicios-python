soma = 0
for i in range(6):
    n = int(input(f'Insira o {(i+1)}° número: '))
    if n % 2 == 0: 
        soma += n

print(soma)