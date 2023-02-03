n = []

for i in range(3):
    n.append(input(f'Insira o {(i + 1)}° número: '))
    
for i in range(3):
    menor = n[0]
    maior = n[0]
    if n[i] <= menor:
        menor = n[i]
    elif n[i] >= maior:
        maior = n[i]

print(f'O menor número é {menor} \nO maior número é {maior}')

