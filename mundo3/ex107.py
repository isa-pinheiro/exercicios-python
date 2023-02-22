import ex107moedas as m

preco = float(input('Insira o preço em real: '))

metade = m.metade(preco)
dobro = m.dobro(preco)
aumentando = m.aumentar(preco)

print(f'Aumentando 10% de {preco} é {aumentando:.1f}')
print(f'O dobro de {preco} é {dobro}')
print(f'A metade de {preco} é {metade}')