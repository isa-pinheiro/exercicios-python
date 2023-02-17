valor = 0
lista =[[], []]

for i in range(7):
    valor = int(input(f'insira o {i + 1}º número: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
    valor = 0
    
print(f'pares: {lista[0]} \nimpares: {lista[1]}')