zero10 = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez']
opcao = None
while opcao != 'n':
    num = int(input('insira um número entre 0 e 10: '))
    if num > 10 or num < 0:
        print('numero invalido')
        continue
    print(f'o número que voce digitou é: {zero10[num]}')
 
    opcao = str(input('voce quer continuar: [s/n]: ')).lower
    
    if opcao != 's' and opcao != 'n':
        print('opçao invalida')
        continue