cont = soma = 0
while True:
    n = int(input('Digite um número(999/Parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A somas dos valores foi {soma} desses {cont} números')
