from random import shuffle
# import random as r
alunos = []

for i in range(4):
   alunos.append(input(f'Digite o {(i+1)}° aluno: '))
        
shuffle(alunos)
print(f'A ordem será {alunos}')