opcao = 0
while opcao != 5:
    n1 = int(input(f'insira o primeiro número: '))
    n2 = int(input(f'insira o segundo número: '))
    opcao = int(input('insira a opção: \n[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair \n'))
    if opcao == 1:
        soma = n1 + n2
        print(f'a soma é {soma}')
    elif opcao == 2:
        mult = n1 * n2
        print(f'a multiplicação é {mult}')
    elif opcao == 3:
        if n1 > n2:
            print(f'o {n1} é maior que {n2}')
        elif n1 < n2:
            print(f'o {n2} é maior que {n1}')
        else:
            print('Os números são iguais')
    elif opcao == 4:
        continue        
    elif opcao == 5:
        break
    else: 
        print('opção inválida. tente novamente')
        
