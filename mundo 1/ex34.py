salario = float(input('Insira o valor do salário: '))

if salario <= 1250:
   aumento = salario * 1.15
else:
    aumento = salario * 1.1
    
print(f'O salário com o aumento fica: {aumento}')