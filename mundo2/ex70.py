opcao = 's'
count_maismil = 0
count_total = 0
barato_preco = 0
barato_nome = ''


while True:
    if opcao != 's' and opcao != 'n':
        print('opcao inválida tente novamente')
        continue
    elif opcao == 'n':
        break
    
    produto = str(input('Insira o produto: '))
    preco = float(input('Insira o preço: '))
    opcao = str(input('Você quer continuar? [S/N]')).lower()
    
    if barato_nome == '' and barato_preco == 0:
        barato_preco = preco
        barato_nome = produto
    elif preco < barato_preco:
        barato_preco = preco
        barato_nome = produto
              
    if preco > 1000:
        count_maismil += 1
        
    count_total += preco
        
print(f'tem {count_maismil} produtos custando mais de mil')
print(f'tem {count_total} foi o total comprado')
print(f'o produto {barato_nome} é o mais barato valendo {barato_preco}')