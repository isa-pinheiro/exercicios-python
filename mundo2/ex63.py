n = int(input('insira quantos termos da sequencia fibonacci voce quer ver: '))
t = []

for i in range(n):
    if i == 0 or i == 1:
        t.append(i)
        print(t[i], end='-> ')
    else:
        t.append(t[i -1] + t[i - 2])
        print(t[i], end='-> ')