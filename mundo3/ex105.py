def analise(*notas, sit = True):
    dados = {}
    dados['Total'] = len(notas)
    dados['Maior'] = max(notas)
    dados['Menor'] = min(notas)
    dados['Média'] = sum(notas)/len(notas)
    
    if sit == True:
        if dados['Média'] >= 7:
            dados['Situação'] = 'APROVADO'
        elif dados['Média'] >= 5:
            dados['Situação'] = 'RECUPERAÇÃO'
        else:
            dados['Situação'] = 'REPROVADO'
    return dados


resultado = analise(7,7,5,7, sit = False)
print(resultado)