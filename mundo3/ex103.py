def campeonato(jogador = '<desconhecido>', gols = 0):
    print(f'O jogador {jogador} fez {gols} no campeonato')
    
j = str(input('insira o nome do jogador: '))
g = str(input('insira o numero de gols: '))

if g.isnumeric and g != '':
    g = int(g)
else:
    g = 0
    

if j == '':
    campeonato(gols = g)
else:
    campeonato(j, g)

