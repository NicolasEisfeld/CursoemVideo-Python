from random import randint
pc = randint(0, 10)
print('''Sou seu computador.....Acabei de pensar em um número entre 0 e 10
Será que você consegue adivinhar qual foi?''')
acerto = False
palpites = 0
while not acerto:
    player = int(input('Qual é o seu palpite?'))
    palpites =+ 1
    if player == pc:
        acerto = True
    else:
        if player < pc:
            print('Mais....Tente mais uma vez.')
        if player > pc:
            print('Menos.....Tente mais uma vez')
print('Acertou com {} tentativas!'.format(palpites))