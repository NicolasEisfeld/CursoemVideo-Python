from random import randint
print('-' * 5, 'Jogo do Par ou Ímpar', '-' * 5)
vezes = 0
while True:
    player = int(input('Digite um número\nDe 1 a 10\n''0/Parar'' :'))
    if player == 0:
        print(f'Você ganhou {vezes} vezes!\nParabéns! ')
        break
    jogada = str(input('Você escolhe ÍMPAR ou PAR? I/P :')).strip().upper()
    while jogada not in 'IP':
        print('JOGADA INVÁLIDA')
        jogada = str(input('Você escolhe ÍMPAR ou Par? I/P :'))
    pc = randint(1, 11)
    resultado = player + pc
    if resultado % 2 == 0:
        if jogada == 'P':
            print(f'Você jogou {player}, e eu joguei {pc}\nE o resultado foi {resultado} , assim deu Par\nPor isso você ganhou!\nJogue Mais!')
            vezes += 1
        else:
            print(f'Você jogou {player}, e eu joguei {pc}\nE o resultado foi {resultado}, assim deu Par\nPor isso eu ganhei!\nTente Novamente!')
            print('GAME OVER ')
    else:
        if jogada == 'I':
            print(f'Você jogou {player}, e eu joguei {pc}\nE o resultado foi {resultado}, assim deu Ímpar\nPor isso você ganhou\nJogue Mais!')
            vezes += 1
        else:
            print(f'Você jogou {player}, e eu joguei {pc}\nE o resultado foi {resultado}, assim deu Ímpar\nPor isso eu ganhei!\nTente Novamente!')
            print('GAME OVER ')

print('-' * 10)
