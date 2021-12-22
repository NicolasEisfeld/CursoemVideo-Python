import random

a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Quarto aluno: ')
lis = [a, b, c, d]
es = random.choice(lis)
print('O aluno escolhido foi: {}'.format(es))
