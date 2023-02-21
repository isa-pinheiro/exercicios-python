def maior(*valores):
    maior = valores[0]
    for i in valores:
        if i > maior:
            maior = i
            
    print(f'o maior valor dado foi {maior}')
    
    
maior(1, 2, 3, 4, 5, 6, 7, 8, 9)
maior(2, 4, 6, 7, 975)
maior(51,623,851,7416,65)
