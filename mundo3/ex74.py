from random import randint
num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('os numeros são:', end=' ')
for i in num:
    print(i, end=' ')
    
print(f'\n{max(num)} é o maior e {min(num)} é o menor')