maior = 0
menor = 0

for i in range(1,6):
    peso = int(input((f'insira o peso da {i}° pessoa: ')))
    if i == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
        
print(f'o maior peso é {maior} \no menor peso é {menor}')