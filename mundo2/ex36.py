valor_casa = int(input('Insira o valor da casa: '))
salario = int(input('Insira o seu salário: '))
anos = int(input('Insira em quantos anos você vai pagar: '))

mensal = valor_casa / anos / 12

if mensal <= (salario * 0.3):
    print('O empréstimo foi aceito')
else:
    print('O empréstimo foi negado')