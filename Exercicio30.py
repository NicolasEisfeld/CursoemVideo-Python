from time import sleep
num = int(input('Me diga um número completo: '))
s = num % 2
print('Esperando...')
sleep(1)
if s == 1:
    print('Seu número é ímpar! ')
else:
    print('Seu número é par! ')

