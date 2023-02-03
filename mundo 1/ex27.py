nome = input('Digite seu nome completo: ').title().strip().split()
print(f'Seu primeiro nome é {nome[0]} \nSeu último nome é {(nome[len(nome) - 1])}')