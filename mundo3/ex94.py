dados = {}
lista = []
mulheres = []
maior = []
while True:
    dados['Nome'] = str(input('insira o nome: '))
    dados['Sexo'] = str(input('insira o sexo[F/M]: ')).lower()
    dados['Idade'] = int(input('insira a idade: '))
    lista.append(dados)
    
    opcao = str(input('Você quer continuar [N para sair]? ')).lower()
    if opcao == 'n':
        break
    dados = {}

print(f'{len(lista)} foram cadastrados')
soma = 0
for i, j in enumerate(lista):
    soma += j['Idade']
    
    if j['Sexo'] == 'f':
        mulheres.append(j['Nome'])
        
    if j['Idade'] >= 18:
        maior.append(j['Idade'])
    
media = soma/len(lista)
print(f'A lista de mulheres cadastradas {mulheres}')
print(f'A media de idade {media}')
print(f'A lista de idades de maior {maior}')
# print(mulheres, media, maior)
# # print(lista)