import random as r
jogadas = ['pedra', 'papel', 'tesoura']
escolha_m = r.randint(0,2)

escolha_u = int(input('Escolha entre: \n[1] Pedra \n[2] Papel \n[3] Tesoura\n'))

if escolha_m == 0:
    if escolha_u == 1:
        print(f'COMPUTADOR ESCOLHEU {jogadas[escolha_m]} \nEMPATE')
    elif escolha_u == 2:
        print(f'COMPUTADOR ESCOLHEU {jogadas[escolha_m]} \nVOCÊ GANHOU')
    elif escolha_u == 3:
        print(f'COMPUTADOR ESCOLHEU {jogadas[escolha_m]} \nVOCÊ PERDEU')
    else:
        print('Opção inválida')
elif escolha_m == 1:
    if escolha_u == 1:
        print(f'COMPUTADOR ESCOLHEU {jogadas[escolha_m]} \nVOCÊ GANHOU')
    elif escolha_u == 2:
        print(f'COMPUTADOR ESCOLHEU {jogadas[escolha_m]} \nEMPATE')
    elif escolha_u == 3:
        print(f'COMPUTADOR ESCOLHEU {jogadas[escolha_m]} \nVOCÊ PERDEU')
    else:
        print('Opção inválida')
elif escolha_m == 2:
    if escolha_u == 1:
        print(f'COMPUTADOR ESCOLHEU {jogadas[escolha_m]} \nVOCÊ PERDEU')
    elif escolha_u == 2:
        print(f'COMPUTADOR ESCOLHEU {jogadas[escolha_m]} \nEMPATE')
    elif escolha_u == 3:
        print(f'COMPUTADOR ESCOLHEU {jogadas[escolha_m]} \nVOCÊ GANHOU')
    else:
        print('Opção inválida')