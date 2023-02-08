opcao = 's'
count_maior = 0
count_homens = 0
count_mulheres = 0

while True:
    if opcao != 's' and opcao != 'n':
        print('opcao inválida tente novamente')
        continue
    elif opcao == 'n':
        break
    
    idade = int(input('Insira a idade: '))
    sexo = str(input('Insira o sexo [M/F]: ')).lower()
    opcao = str(input('Você quer continuar? [S/N]')).lower()
    
    if idade > 18:
        count_maior += 1
        
    if sexo == 'm':
        count_homens += 1
        
    if sexo == 'f' and idade < 20:
        count_mulheres += 1
        
print(f'tem {count_mulheres} mulheres com menos de 20 anos')
print(f'tem {count_maior} pessoas com mais de 18')
print(f'tem {count_homens} homens no total')