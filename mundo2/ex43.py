peso = float(input('Insira seu peso em quilo: '))
altura = float(input('Insira sua altura em metros:  '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')