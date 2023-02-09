num =(int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')), int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')))
print(f'os números digitados foram {num}')
print(f'o número nove apareceu {num.count(9)} vezes')

if 3 in num:
    print(f'o número 3 apareceu a primeria vez na posiçao {num.index(3)}')
else:
    print('o numero 3 nao foi digitado')
print('os valores pares digitados são: ', end=' ')
for i in num:
    if i % 2 == 0:
        print(f'{i}', end=' ' )