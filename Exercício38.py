num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
if num1 > num2:
    print('O número maior entre eles é\n          \-_{}_-/'.format(num1))
elif num2 > num1:
    print('O número maior entre eles é\n          \-_{}_-/'.format(num2))
elif num1 == num2:
    print('Os dois números são parcialmente iguais')