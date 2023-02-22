def verificaInteiro(txt):
    while True:
        try:
            n = int(input(txt))
        except:
            print('Erro. Insira um número inteiro válido')
            continue
        else: 
            return n
        
def verificaFloat(txt):
    while True:
        try:
            n = float(input(txt))
        except:
            print('Erro. Insira um número real válido')
            continue
        else: 
            return n

i = verificaInteiro('Insira um número inteiro: ')
r = verificaFloat('Insira um número real: ')
print(f'seu inteiro é {i}')
print(f'seu real é {r}')
