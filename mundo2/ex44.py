valor = float(input('Insira o valor do produto: '))
opcao = int(input('Insira uma opção de pagamento: \n[1] Dinheiro/Cheque \n[2] Cartão 1x \n[3] Cartão 2x \n[4] Cartão 3x ou mais'))

if opcao == 1:
    print(f'O valor a ser pago é {valor * 0.9}')
elif opcao == 2:
    print(f'O valor a ser pago é {valor * 0.95}')
elif opcao == 3:
    print(f'O valor a ser pago é {valor}')
elif opcao == 4:
    print(f'O valor a ser pago é {valor * 1.2}')
else:
    print('Opção inválida')