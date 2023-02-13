val = []
count = 0
opcao = None

while opcao != 'n':
    val.append(int(input('insira um numero: ')))
    opcao = str(input('voce quer continuar? [s/n]'))
    if opcao != 's' and opcao != 'n':
        print('opcao invalida. tente novamente')
        continue

 
print(f'{len(val)} foram adicionados')
print(f'{sorted(val, reverse=True)} foram adicionados')

for i in val:
    if i == 5:
        count += 1
print(f'{count} digitos sao iguais a 5')