s = str(input('Gênero da pessoa: M/F ')).upper()[0].strip()
while s not in 'MF':
    print('Dados Inválidos....')
    s = str(input('Gênero da pessoa M/F:')).strip().upper()[0]
print('Gênero {} registrado com sucesso!'.format(s))


