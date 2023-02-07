nome = []
idade = []
sexo = []
media_idade = 0
velho = ''
velho_idade = 0
count = 0
for i in range(4):
    idade.append(int(input(f'Insira a idade do {i + 1}°: ')))
    nome.append(str(input(  f'Insira o nome do {i + 1}°: ')))
    sexo.append(int(input(f'Insira: \n[1] Feminino \n[2] Masculino\n')))
    media_idade += idade[i]
    
    if sexo[i] == 2:
        if idade[i] >= idade[i-1]:
            velho = nome[i]
            velho_idade = idade[i]
    elif sexo[i] == 1:
        if idade[i] < 20:
            count += 1

print(f'Tem {count} mulheres com menos de 20 anos')
print(f'{velho} é o homem mais velho com {velho_idade} anos')