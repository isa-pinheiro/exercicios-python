frase = str(input('Insira uma frase: ')).strip().lower()
qtd = frase.count('a')
posi = frase.find('a') + 1
posf = frase.rfind('a') + 1
print(f'A letra A aparece {qtd} vezes')
print(f'A primeira posição do A é {posi}')
print(f'A primeira posição do A é {posf}')