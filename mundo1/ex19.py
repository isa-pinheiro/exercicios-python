import random as r
n1 = str(input('Insira o primeiro nome: '))
n2 = str(input('Insira o segundo nome: '))
n3 = str(input('Insira o terceiro nome:'))
lista = [n1, n2, n3]

print('O nome escolhido foi: ', r.choice(lista))
