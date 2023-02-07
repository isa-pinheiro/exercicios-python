numero = int(input('Insira um número para calcular seu fatorial: '))
fatorial = 1

for i in range(numero):
    fatorial *= (numero - i)
    
print(f'o fatorial é {fatorial}')