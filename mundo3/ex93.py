dados = {}

dados['Nome'] = str(input('Nome: '))
dados['Gols'] = []
dados['Partidas'] = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
dados['Total'] = 0
for i in range(dados['Partidas']):
    gol = int(input(f'Quantos gols na partida {(i+1)}: '))
    dados['Gols'].append(gol)
    dados['Total'] += gol

print('=' * 30)
print(dados)
print('=' * 30)
for i, j in dados.items():
    if j == dados['Partidas']:
        continue
    else:
        print(f'O item {i} tem valor {j}')
print('=' * 30)
print(f'O jogador {dados["Nome"]} jogou {dados["Partidas"]}')
for i, j in enumerate(dados['Gols']):
    print(f'Na partida {i+1} fez {j} gols')
print('=' * 30)

