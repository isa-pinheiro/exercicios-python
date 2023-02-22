import ex108moedas as m

preco = float(input('Insira o preço em real: '))

metade = m.metade(preco)
dobro = m.dobro(preco)
aumentando = f'{m.aumentar(preco):.1f}'

print(f'Aumentando 10% de {m.cifrao(preco)} é {m.cifrao(aumentando)}')
print(f'O dobro de {m.cifrao(preco)} é {m.cifrao(dobro)}')
print(f'A metade de {m.cifrao(preco)} é {m.cifrao(metade)}')