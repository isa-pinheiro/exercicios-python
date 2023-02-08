from random import randint

while True:
    n = int(input('insira um número: '))
    n_c = randint(0,11)
    ip = str(input('Ímpar ou Par [I/P]: ')).upper()
    soma = n_c + n
    if soma % 2:
        if ip =='I':
            print('você venceu.')
            continue
        elif ip == 'P':
            print('você perdeu')
            break
        else:
            print('opção inválida')
            continue
    elif not (soma % 2):
        if ip =='I':
            print('você venceu.')
            continue
        elif ip == 'P':
            print('você perdeu')
            break
        else:
            print('opção inválida')
            continue