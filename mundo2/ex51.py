n = float(input('insira o primeiro termo da pa: '))
r = float(input('insira a razão da pa: '))
print(n, end='-> ')
for i in range(10):
    n += r
    print(n, end='-> ')
    
print('fim')