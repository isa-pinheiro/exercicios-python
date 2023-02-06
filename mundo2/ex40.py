n1=float(input('Insira a primeira nota: '))
n2=float(input('Insira a segunda nota: '))

media = (n1 + n2) / 2

if media > 7.0:
    print('APROVADO')
elif media < 5.0:
    print('REPROVADO')
else:
    print('RECUPERAÇÃO')