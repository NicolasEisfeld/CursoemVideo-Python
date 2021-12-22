import random
from time import sleep
op = int(input('''=====Qual dificuldade?=====
[ 1 ] MÉDIO
[ 2 ] IMPOSSÍVEL!!
Qual dificuldade? '''))
if op == 1:
    itens = ('Pedra' , 'Papel' , 'Tesoura')
    pc = random.randint(0 , 2)
    jo = int(input('''-=-=Suas Opções:=-=-
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA
    Qual é sua jogada? '''))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!')
    print('-=' * 11)
    print('Computador jogou {}'.format(itens[pc]))
    print('Jogador jogou {}'.format(itens[jo]))
    print('-=' * 11)
    if pc == 0:
        if jo == 0:
            sleep(1)
            print('EMPATE')
        elif jo == 1:
            sleep(1)
            print('JOGADOR VENCE!')
        elif jo == 2:
            sleep(1)
            print('COMPUTADOR VENCE!')
        else:
            sleep(1)
            print('Jogada inválida!')
    elif pc == 1:
        if jo == 0:
            sleep(1)
            print('COMPUTADOR VENCE!')
        elif jo == 1:
            sleep(1)
            print('EMPATE')
        elif jo == 2:
            sleep(1)
            print('JOGADOR VENCE!')
        else:
            print('Jogada inválida!')
    elif pc == 2:
        if jo == 0:
            sleep(1)
            print('JOGADOR VENCE!')
        elif jo == 1:
            sleep(1)
            print('COMPUTADOR VENCE!')
        elif jo == 2:
            sleep(1)
            print('EMPATE')
        else:
            print('Jogada inválida!')
elif op == 2:
    itens = ('Pedra', 'Papel', 'Tesoura')
    pc = random.randint(0, 2)
    jo = int(input('''-=-=Suas Opções:=-=-
        [ 0 ] PEDRA
        [ 1 ] PAPEL
        [ 2 ] TESOURA
        Qual é sua jogada? '''))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!')
    print('-=' * 22)
    if jo == 0:
        print('O Jogador jogou PEDRA, e o Computador jogou PAPEL')
        print('Por isso eu...')
        sleep(1)
        print('GANHEI!')
    elif jo == 1:
        print('O Jogador jogou PAPEL, e o Computador jogou TESOURA')
        print('Por isso eu...')
        sleep(1)
        print('GANHEI!')
    elif jo == 2:
        print('O Jogador jogou TESOURA, e o Computador jogou PEDRA ')
        print('Por isso eu...')
        sleep(1)
        print('GANHEI!')
    elif jo == 3:
        print('O Computador jogou {}, e o Jogador jogou ??? '.format(itens[pc]))
        print('Por isso eu...')
        sleep(2)
        print('Como assim?! PERDI!')
    else:
        print('Jogada inválida!')
    print('-=' * 22)
else:
    print('Jogada inválida!')
