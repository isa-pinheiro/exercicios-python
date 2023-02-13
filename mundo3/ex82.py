val = []
pares = []
impar =[]
opcao = None
while opcao != 'n':
    val.append(int(input('insira um numero: ')))
    opcao = str(input('voce quer continuar? [s/n]'))
    if opcao != 's' and opcao != 'n':
        print('opcao invalida. tente novamente')
        continue

for i in val:
    if i % 2 == 0:
        pares.append(i)
    else:
        impar.append(i)

print(f'{val} é a lista completa')
print(f'{pares} são os números pares')
print(f'{impar} são os números impar')