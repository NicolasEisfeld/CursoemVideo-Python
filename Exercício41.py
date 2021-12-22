from datetime import date
Ano = int(input('Digite o ano que você nasceu: '))
A = date.today().year
i = A - Ano
print('Esse Atleta tem {} Anos'.format(i))
if i <= 9:
    print('Classificação: MIRIM')
elif i > 9 and i < 14:
    print('Classificação: INFANTIL')
elif i > 14 and i < 19:
    print('Classificação: JUNIOR')
elif i > 19 and i < 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')