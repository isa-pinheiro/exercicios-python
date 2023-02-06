# n = str(input('Insira um número: *contendo 4 dígitos'))

# print(f'A unidade {n[3]} \nA dezena {n[2]} \nA centena {n[1]} \nO milhar {n[0]}')

n = int(input('Insira um número: '))
print(f'A unidade {(n % 10)} \nA dezena {((n % 100) // 10)} \nA centena {((n % 1000) // 100)} \nO milhar {(n // 1000)}')
