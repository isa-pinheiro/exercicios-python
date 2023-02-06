primeiro = int((input('Insira o primeiro número:')))
segundo = int((input('Insira o segundo número:')))

if primeiro > segundo:
    print('O primeiro é maior')
elif segundo > primeiro:
    print('O segundo é maior')
else: 
    print('Os dois são iguais')