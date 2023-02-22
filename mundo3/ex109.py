import ex109moedas as m

preco = float(input('Insira o preço em real: '))

metade = m.metade(preco, form=True)
dobro = m.dobro(preco, form=True)
aumentando = f'{m.aumentar(preco,form=True)}'

print(f'Aumentando 10% de {preco} é {aumentando}')
print(f'O dobro de {preco} é {dobro}')
print(f'A metade de {preco} é {metade}')