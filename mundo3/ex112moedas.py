def aumento(n, a, form = False):
    aumento = n * (1 + (a/100))
    return aumento if form is False else cifrao(aumento)


def reducao(n, r, form = False):
    reducao = n * (1 - (r/100))
    return reducao if form is False else cifrao(reducao)


def dobro(n, form = False):
    dobroden = n * 2
    return dobroden if form is False else cifrao(dobroden)


def metade(n, form = False):
    metadeden = n / 2
    return metadeden if form is False else cifrao(metadeden)


def cifrao(n = 0, moeda='R$'):
    return f'{moeda}{n}'


def resumo(n, aum, red):
    a = aumento(n, aum, True)
    r = reducao(n, red, True)
    m = metade(n, True)
    d = dobro(n, True)
    n = cifrao(n)
    print(f'{n} é o preço analisado')
    print(f'{a} é o aumento de {aum}%')
    print(f'{r} é a redução de {red}%')
    print(f'{m} é a metade do preço')
    print(f'{d} é o dobro do preço')
    
    
def leiaDinheiro(txt):
    verificado = False
    while True:
        n = input(txt).replace(',', '.')
        if n.isalpha() and n.strip() == '':
            print('Erro. Insira um número válido.')
        else:
            verificado = True
            real = float(n)
        
        if verificado:
            break
    return real