numero = int(input('Digite um número: '))
count = 0
for i in range(1,numero):
    print(i)
    if (numero % i == 0):
        count += 1
        
if count == 1:
        print(f'O número {numero} é primo, só é divisivel por 1 e ele mesmo')
elif count > 2:
        print(f'O número {numero} é divisível por {(count + 1)} números')
else: 
        print('Algo está errado, tente novamente')