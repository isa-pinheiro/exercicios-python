n = []
opcao = None
while opcao != 'n':
    var = int(input('digite um número: '))
    if var in n:
        print('valor ja esta na lista. tente outro')
        continue
    else: 
        n.append(var)
    opcao = str(input('voce quer continuar? [s/n]'))
    if opcao != 's' and opcao != 'n':
        print('opcao invalida. tente novamente')
        continue

print(f'voce digitou os valores {sorted(n)}')