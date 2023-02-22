def voto(idade):
    if idade < 16:
        return 'VOTO NEGADO'
    elif idade < 18:
        return 'VOTO OPCIONAL'
    elif idade < 70:
        return 'VOTO OBRIGATÓRIO'
    else:
        return 'VOTO OPCIONAL'
    
ano = int(input('Insira o ano que você nasceu: '))
idade = 2023 - ano
resultado = voto(idade)

print(f'Com {idade} seu voto é {resultado}')