from random import  randint
from time import sleep
pc = randint(0, 5)
print('<\/>' * 20)
print('Tente adivinhar qual número pensei:de 0 a 5')
print('<\/>' * 20)
player = int(input('Qual número eu pensei? '))
print('PrOcEsSaNdO...')
sleep(2)
if pc == player:
    print('Você acertou!*PARABÉNS*')
else:
    print('Você errou!Tente novamente...')
    print('Você pensou no número {} e eu pensei no número {}\nPor isso você perdeu'.format(player , pc))


