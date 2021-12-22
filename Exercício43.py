p = float(input('Qual é seu peso? (kg): '))
a = float(input('Qual é sua altura? (.m): '))
imc = p / (a ** 2)
print('O imc dessa pessoa é {:.2f}\nPor isso ela:'.format(imc))
if imc >= 18.5 and imc < 25:
    print('Está na massa ideal!')
elif imc < 18.5:
    print('Precisa comer mais!')
elif 25 <= imc < 30:
    print('Está sobrepeso!')
elif 30 <= imc < 40:
    print('Está iniciando a Obesidade!')
elif imc >= 40:
    print('Está na OBESIDADE MÓRBIDA!')