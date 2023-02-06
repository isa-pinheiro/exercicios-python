idade = int(input('insira quantos anos você tem:'))

if idade == 18:
    print('Está na hora de se alistar')
elif idade < 18:
    print('Ainda vai precisar se alistar')
elif idade > 18:
    print('Já passou da idade de se alistar')