alunodict = {}
alunodict['nome'] = str(input('NOME: '))
alunodict['media'] = float(input('MÉDIA: '))

if alunodict['media'] >= 7:
    alunodict['situaçao'] = 'aprovado'
elif alunodict['media'] >= 5:
    alunodict['situaçao'] = 'recuperaçao'
else:
    alunodict['situaçao'] = 'reprovado'
    
for i, j in alunodict.items():
    print(f'{i} é igual {j}')