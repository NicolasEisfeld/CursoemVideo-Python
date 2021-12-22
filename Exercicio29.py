print('-_-' * 10 )
km = float(input('Você está dirigindo em qual velocidade? '))
print('-_-' * 10)
if km < 65:
    print('Certo!Está tudo otimo!')
else:
    print('Eita!Você ultrapassou a velocidade permitida!')
    print('Você receberá uma multa de R${:.2f} por ultrapassar 65km/h'.format((km - 65) * 65 ))
print('Dirija com segurança! ')

