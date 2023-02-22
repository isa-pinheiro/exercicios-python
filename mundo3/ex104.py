def verificaInteiro(txt):
    verificado = False
    inteiro = 0
    while True:
        n = input(txt)
        if n.isnumeric() and n.strip() != 0:
            verificado = True
            inteiro = int(n)
        else:
            print('Erro. Insira um inteiro.')
        
        if verificado:
            break
    return inteiro

n = verificaInteiro('Insira um inteiro: ')

print(f'seu inteiro é {n}')