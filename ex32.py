ano = int(input('Insira o ano que você quer checar: '))

if ano % 4 == 0 or ano % 100 != 0 and ano % 400 == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')  