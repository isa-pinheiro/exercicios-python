soma = 0

for i in range(500):
    if i % 3 == 0 and i % 2 == 1:
        soma += i
        
print(soma)