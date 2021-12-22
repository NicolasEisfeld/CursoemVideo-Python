primeiro = int(input('PRIMEIRO TERMO: '))
segundo = int(input('RAZÃO: '))
décimo = primeiro + (10-1) * segundo
for c in range(primeiro, décimo, segundo):
    print('{} '.format(c), end=' ')
print('ACABOU')
