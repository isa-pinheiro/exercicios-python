expressao = str(input('digite uma expressao: '))
buff = []

for i in expressao:
    if i == '(':
        buff.append('(')
    elif i == ')':
        if len(buff) > 0:
            buff.pop()
        else:
            buff.append(')')

if buff == 0:
    print('a expressao é valida')
else:
    print('a expressao não esta valida')