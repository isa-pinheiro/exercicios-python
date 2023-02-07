from random import randint

numero_c = randint(0, 10)
numero_u = int(input('insira um número de um a 10: '))
while numero_c != numero_u:
    if numero_c > numero_u:
        numero_u = int(input('o número é maior. tente novamente. \ninsira: '))
    elif numero_c < numero_u:
        numero_u = int(input('o número é menor. tente novamente. \ninsira: '))
        
print(f'Acertou. O número era {numero_c}')