km = int(input('Quantos km você percorreu essa viagem? '))
if km < 200:
    print('Você tem o total a pagar R${:.2f} '.format(km / 2))
else:
    print('Você tem o total a pagar R${:.2f}'.format(km / 1.95))