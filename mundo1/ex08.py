n = float(input('Insira uma distância em metros: '))
print('A medida {:.1f}m é equivalente:'.format(n)),
print('{:1f}Km \n{:.1f}hm \n{:.1f}dam \n{:.1f}dm \n{:.1f}cm \n{:.1f}mm'.format((n/1000), (n/100), (n/10), (n*10), (n*100), (n*1000)))