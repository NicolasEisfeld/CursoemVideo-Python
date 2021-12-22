soma = 0
media = 0
maiorhomem = 0
nomevelho = ''
mulheres20 = 0
for pessoas in range(1, 5):
    nome = str(input('Qual o nome da {} pessoa?'.format(pessoas))).strip()
    idade = int(input('Qual a idade da {} pessoa?'.format(pessoas)))
    genero = str(input('''Qual o gênero da {} pessoa 
    [ M ] Masculino
    [ F ] Feminino
    ---'''.format(pessoas)))
    soma += idade
    if pessoas == 1 and genero in 'Mm':
        maiorhomem = idade
        nomevelho = nome
    if genero in 'mM' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if genero in 'Ff' and idade < 20:
        mulheres20 += 1
media = soma / 4
print('A média da idade do grupo é {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorhomem, nomevelho))
print('Ao todo são {} mulheres com menoos de 20 anos'.format(mulheres20))