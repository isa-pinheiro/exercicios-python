import math as m
a = float(input('Insira o valor do ângulo em graus: '))
print('O seno é {:.2f} \nO cosseno é {:.2f} \nA tangente é {:.2f}'.format(m.sin(m.radians(a)), m.cos(m.radians(a)), m.tan(m.radians(a))))