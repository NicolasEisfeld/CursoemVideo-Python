d = int(input('Digite um número: '))
u = d // 1 % 10
de = d // 10 % 10
c = d // 100 % 10
m = d // 1000 % 10
print('Analizando o número {}\nEle tem:'.format(d))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(de))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
