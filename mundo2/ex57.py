sexo = str(input('insira seu sexo: [F/M]: ')).upper()
while sexo not in 'fFmM':
    sexo = str(input('Dado inválido. Tente novamente.')).upper()

print(f'o sexo {sexo} foi registrado')