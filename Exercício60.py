# bom dia!
n = int(input('Digite um número\nPara calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! ='.format(n))
while c > 0:
    print('{} x'.format(c), end='')
    print(' x ' if  c > 1 else '  =  ', end='')
    f = f * c
    c -= 1
print('{}'.format(f))