import math as m
co = float(input('Insira o tamanho do cateto oposto: '))
ca = float(input('Insira o tamanho do cateto adjacente: '))
print('A hipotenusa vale: {:.2f}'.format(m.hypot(co,ca)))