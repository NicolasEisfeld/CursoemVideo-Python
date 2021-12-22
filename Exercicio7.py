n1 = float(input('qual foi sua primeira nota? '))
n2 = float(input('qual foi sua segunda nota? '))
n3 = n1 + n2
n4 = n3 / 2
print('a média de {} e {} \nÉ {:.1f} '.format(n1, n2, n4))
if n4 >= 6.0:
    print('Sua média foi boa! Parabéns')
else:
    print('Sua nota não foi boa! Estude mais!')
