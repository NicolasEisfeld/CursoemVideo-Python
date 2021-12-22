p = int(input('Primeiro Valor: '))
s = int(input('Segundo Valor: '))
t = int(input('Terceiro Valor: '))
memo = p
if s < p and s < t:
    memo = s
if t < p and t < s:
    memo = t
maio = p
if s > p and s > t:
    maio = s
if t > p and t > s:
    maio = t
print('O menor valor digitado foi:\n{}\nO maior valor digitado foi:\n{}'.format(memo, maio))

