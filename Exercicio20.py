import random

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lis = [n1, n2, n3, n4]
random.shuffle(lis)
print('A ordem de apresentaçao sera:')
print(lis)


