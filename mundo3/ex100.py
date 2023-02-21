from random import randint

def sorteando(lista):
    print('sorteando 5 valores: ', end='')
    for i in range(5):
        num = randint(1, 10)
        lista.append(num)
        print(num, end=' ')
    print('fim.')
    
def pares(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos pares na lista {lista} é igual {soma}')
    

lista1 = []
sorteando(lista1)
pares(lista1)