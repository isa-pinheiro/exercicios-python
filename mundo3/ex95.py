jogador = {}
lista = []
gols = []

while True:
    jogador['Nome'] = str(input('Insira o nome do jogador: '))
    partidas = int(input(f'insira a quantidade de partidas {jogador["Nome"]} jogou: '))
    
    for i in range(partidas):
        gols.append(int(input(f'Insira quantos gols {jogador["Nome"]} fez na {i+1}° partida:')))
        
    jogador['Gols'] = gols[:]
    jogador['Total de Gols'] = sum(gols)
    
    lista.append(jogador)
    jogador = {}
    gols = []
    
    opcao = str(input('Voce quer continuar [S/N]?')).lower()
    if opcao == 'n':
        break

# print(lista)
print('='*30)
for i, j in enumerate(lista):
    print(i, end='    ')
    print(j["Nome"], end='    ')
    print(j["Gols"], end='    ')
    print(j["Total de Gols"], end='    ')
    print()
    
print('='*30)
while opcao != 999:
    escolha = int(input('voce quer ver status de que jogador? [999 para parar]'))
    opcao = escolha
    print(f'levantamento do jogador {lista[escolha]["Nome"]}')
    for i, j in enumerate(lista[escolha]['Gols']):
        print(f'No jogo {i+1} ele fez {j} gols')
    

    
