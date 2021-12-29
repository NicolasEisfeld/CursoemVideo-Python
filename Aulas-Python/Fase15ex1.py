# cont = 1
# while True:
#   print(cont, '->', end='')
#  cont + 1
# print('Acabou')

n = S = 0
while True:
    n = int(input('Digite um Número: '))
    if n == 999:
        break
    S += n
print(f'A soma vale {S}')
# Novo Método de Manipulação
