d = float(input('Por quantos dias você alugou o carro?'))
k = float(input('Quantos Kms rodados?'))
a = d * 60
r = k * 0.15
p = r + a
print('O total a pagar é de R${:.2f}!'.format(p))

