print('_--_' * 20 )
p = int(input('Preço das Compras: R$'))
print('Formas de PAGAMENTO:\n[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista no cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão ')
r = int(input('Qual é sua opção? '))
if r == 1:
    t = p - (p * 10 / 100)
elif r == 2:
    t = p - (p * 5 / 100)
elif r == 3:
    t = p
    parcela = t / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcela))
elif r == 4:
    t = p + (p * 20 / 100)
    topar = int(input('Quantas parcelas? '))
    parcela = t / topar
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(topar, parcela))
else:
    t = 0
    print('OPÇÃO INVALIDA!Tente Novamente!')

print('Sua compra de R${:.2f}\nVai custar R${:.2f} no final.'.format(p , t))

