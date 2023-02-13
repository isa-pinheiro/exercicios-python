temp = []
pessoapeso = []
mai = 0
men = 0
while True:
    temp.append(str(input('insira o nome: '))) 
    temp.append(int(input('insira o peso: '))) 
    if len(pessoapeso) == 0:
        mai = temp[1]
        men = temp[1]
    elif temp[1] > mai:
        mai = temp[1]
    elif temp[1] < men:
        men = temp[1]
    pessoapeso.append(temp[:])
    temp.clear()
    opcao = str(input('voce quer continuar [s/n]? '))
    if opcao in 'Nn':
        break
pessoasmin = []
pessoasmai = []
print(f'foram cadastradas {len(pessoapeso)} pessoas')
for i in pessoapeso:
    if i[1] == men:
        pessoasmin.append(i[0])
    elif i[1] == mai:
        pessoasmai.append(i[0])
print(f'as pessoas com o menor peso {men} sao {pessoasmin}')
print(f'as pessoas com o maior peso {mai} sao {pessoasmai}')