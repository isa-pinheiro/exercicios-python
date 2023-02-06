numero = int(input('Insira um número inteiro: '))
selecao = input('Digite para converter: \n[1] Binário \n[2] Octal \n[3] Hexadecimal: \n')

if selecao == '1':
    print(f'{bin(numero)}')
elif selecao == '2':
    print(f'{oct(numero)}')
elif selecao == '3':
    print(f'{hex(numero)}')
else:
    print(f'Essa seleção é inválida')