def aumentar(n, form = False):
    dezporden = n * 1.1
    return dezporden if form is False else cifrao(dezporden)
    
def dobro(n, form = False):
    dobroden = n * 2
    return dobroden if form is False else cifrao(dobroden)

def metade(n, form = False):
    metadeden = n / 2
    return metadeden if form is False else cifrao(metadeden)

def cifrao(preco = 0, moeda='R$'):
    return f'{moeda}{preco}'