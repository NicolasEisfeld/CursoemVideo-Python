s = float(input('Digite seu Sálario: R$'))
if s <= 1250:
    n = s + (s * 15 / 100)
else:
    n = s + (s * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(s , n))
