from datetime import date
at = date.today().year
year = int(input('Qual o ano que você nasceu? '))
id = at - year
print('Quem nasceu em {} tem {} anos em {}'.format(year,id,at))
if id == 18:
    print('Está na hora de se ALISTAR!')
elif id < 18:
    s = 18 - id
    a = at + s
    print('Você ainda não tem 18 anos!Ainda faltam {} anos para se alistar. '.format(s))
    print('Seu alistamento será no ano {} '.format(a))
elif id > 18:
    s = id - 18
    a = at - s
    print('Você deveria ter se alistado há {} anos'.format(s))