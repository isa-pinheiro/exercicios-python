count = 0

for i in range(1,8):
    ano = int(input(f'Insira o ano do nascimento da {i}° pessoa: '))
    if (2023 - ano) >= 18:
        count += 1

print(f'De 7 pessoas, {count} são maiores de idade e {7-count} são menores')