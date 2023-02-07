count = 0
num = float(input('insira o primeiro termo da pa: '))
razao = float(input('insira a razao da pa: '))
total = 0
termos = 10
print(num, end='-> ')
while termos != 0:
    total += termos
    while count < total:
        num += razao
        print(num, end='-> ')
        count += 1  
    print('pause')
    termos = int(input('quantos termos a mais você quer ver?'))  
print('fim')

print('fim')