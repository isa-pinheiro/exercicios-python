opcao = 's'
soma = 0
count = 0
n = 0
media = 0
maior = 0
menor = 0
while opcao != 'n':
    n = int(input('insira um número: '))    
    opcao = str(input('Você quer continuar [S/N]: ' )).lower()
    if opcao != 's' and opcao != 'n':
        print('opção inválida. tente novamente')
        continue
    
    soma += n
    count += 1
    media = soma /count
    
    if count == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n    
   
    
        
print(f'voce digitou {count} números, a soma é {soma} e a media é {media}')
print(f'o maior é {maior} e o menor é {menor}')