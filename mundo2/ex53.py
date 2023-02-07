palavra = str(input('insira uma frase: ')).strip().upper().split()
juntos = ''.join(palavra)
inverso_array = []

for i in range(1, len(juntos) + 1):
    inverso_array.append(juntos[-i])

inverso = ''.join(inverso_array)


if inverso == juntos:
    print(f'sua frase é {juntos} e o inverso é {inverso} \nsão palíndromos')
else:
    print(f'sua frase é {juntos} e o inverso é {inverso} \nnão são palíndromos')

