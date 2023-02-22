def fatorial (n, show = False):
    f = 1
    s = ''
    for i in range(n, 0, -1):
        f *= i
    if show == False:
        return f
    elif show == True:
        for i in range(n, -1, -1):
            if i > 1:
                s += f'{i} x '
            elif i == 1: 
                s += f'{i} = '
            else:
                s += f'{f}'
        return s


n = fatorial(5, True)
n1 = fatorial (5)
print(n)
print(n1)