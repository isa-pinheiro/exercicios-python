count = 0
num = float(input('insira o primeiro termo da pa: '))
razao = float(input('insira a razao da pa: '))
print(num, end='-> ')
while count < 9:
    num += razao
    print(num, end='-> ')
    count += 1

print('fim')