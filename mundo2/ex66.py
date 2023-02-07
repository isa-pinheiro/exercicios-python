soma = 0
count = 0
n = 0
while True:
    n = int(input('insira um número [999 para sair]: '))
    
    if n != 999:
        soma += n
        count += 1
    
    if n == 999:
        break
        
print(f'voce digitou {count} e a soma é {soma}')