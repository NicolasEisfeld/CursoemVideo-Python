n = int(input('Digite seu número inteiro: '))
print('\033[1;31mEscolha uma das bases para converter:\033[m\n[ 1 ] converter para BÍNARIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL')
e = int(input('Sua opção: '))
if e == 1:
    print(' {} convertido para BÍNARIO é igual a {}'.format(n, bin(n)[2:]))
elif e == 2:
    print(' {} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif e == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção invalida, tente novamente....')

