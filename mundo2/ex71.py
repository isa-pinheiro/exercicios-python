valor = int(input('insira o valor a ser sacado: '))

count_cedula = valor // 50
print(f'{count_cedula} de 50')
sobra = valor % 50
count_cedula = sobra // 20
print(f'{count_cedula} de 20')
sobra %= 20
count_cedula = sobra // 10
print(f'{count_cedula} de 10')
sobra %= 10
print(f'{sobra} de 1')

