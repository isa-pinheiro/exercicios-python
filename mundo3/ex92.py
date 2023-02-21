pessoa = {}

pessoa['Nome'] = str(input('Nome: '))
pessoa['Ano de Nascimento'] = int(input('Ano de nascimento: '))
pessoa['Idade'] = 2023 - pessoa['Ano de Nascimento']
pessoa['Carteira de Trabalho'] = int(input('Carteira de Trabalho [0 se não existir]'))

if pessoa['Carteira de Trabalho'] != 0:
    pessoa['Ano de Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Aposentadoria'] = pessoa['Idade'] + pessoa['Ano de Contratação: '] + 35 - 2023
    pessoa['Salário'] = float(input('Salário: '))


for i, j in pessoa.items():
    if j == pessoa['Ano de Nascimento']:
        continue
    else:
        print(f'O {i} tem valor {j}')