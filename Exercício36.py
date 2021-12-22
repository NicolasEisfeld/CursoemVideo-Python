home = float(input('Digite o valor da casa: R$'))
s = float(input('Sálario do comprador: R$'))
a = int(input('Quantos anos vai pagar? '))
p = home / (a * 12)
m = s * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos\nA prestação será de R${:.2f}'.format(home,a,p))
if p <= m:
    print('Empréstimo CONSEDIDO!')
else:
    print('Empréstimo NEGADO!')

