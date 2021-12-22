'''for c in range(1, 5):
    n = int(input('Digite um Valor: '))
print('FIM')'''
n = 1
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer Continuar? (N/S)')).upper()
print('Fim')