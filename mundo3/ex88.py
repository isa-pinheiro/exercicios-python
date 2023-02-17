from random import randint
qtdJogos = int(input(f'insira quantos jogos você quer sorteado: '))
count = 1
numTotal = 0
num = []
jogos = []

while count <= qtdJogos:
    for i in range(6):
        add = randint(1, 60)
        num.append(add)
    num.sort()
    jogos.append(num[:])
    num.clear()
    count += 1
    
for i in range(qtdJogos):
    print(f'o jogo {i+1}: {jogos[i]}')