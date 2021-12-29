while True:
    n = int(input('Digite um número, e irá aparecer a tabuada dela: '))
    if n < 0: break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
print('Obrigado por testar meu programa!volte sempre!')
