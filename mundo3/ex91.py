from random import randint
from operator import itemgetter
jogadores = {'jogador 1': randint(1,10),
             'jogador 2': randint(1,10),
             'jogador 3': randint(1,10),
             'jogador 4': randint(1,10)
}
for i, j in jogadores.items():
    print(f'{i} tirou {j}')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i, j in jogadores.items():
    print(f'{i} tirou {j}')