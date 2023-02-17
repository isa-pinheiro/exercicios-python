opcao = None
sair = None
lista = []
dados = []

while sair != 's':
    nome = str(input('NOME: '))
    nota1 = float(input('NOTA 1: '))
    nota2 = float(input('NOTA 2: '))
    media = (nota2 + nota1)/2
    dados.append(nome)
    dados.append(media)
    dados.append(nota1)
    dados.append(nota2)
    lista.append(dados[:])
    dados.clear()
    sair = str(input('Você gostaria de sair[s/n]? ')).lower()
    if sair != 'n' and sair != 's':
        print('opcao invalida. tente novamente.')
        continue

print(lista)
print(f'{"No":<4}{"Nome":<10}{"Média":>8}')
for i, j in enumerate(lista):
    print(f'{i:<4}{j[0]:<10}{j[1]:>8.1f}')

while True:
    opcao = int(input('Mostrar notas de qual aluno? [999 para sair]'))
    if opcao != 999:
        print(f'notas de {lista[opcao][2]} são {lista[opcao][3]}')
    elif opcao == 999:
        break
        
