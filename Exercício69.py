dezoitoanos = homens = mulheresmenor = 0
while True:
    idade = int(input('Qual é sua idade? '))
    if idade > 18:
        dezoitoanos += 1
    sexo = str(input('Qual é seu sexo? M/F: '))
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        if idade < 20:
            mulheresmenor += 1
    resposta = str(input('Quer continuar? S/N: ')).strip().upper()
    if resposta == 'N':
        print(f'O total de mulheres com menos de 20 anos foi {mulheresmenor}, {homens} homens foram cadastrados e foram cadastradas {dezoitoanos} pessoas com mais de 18 anos')
        break
