nota1 = float(input('Sua nota do Primeiro Trimestre: '))
nota2 = float(input('Sua nota do Segundo Trimestre: '))
nota3 = float(input('Sua nota do Terceiro Trimestre: '))
media = (nota1 + nota2 + nota3) / 3
print('Analizando a sua Primeira nota({:.2f})\nSua Segunda nota({:.2f})\nSua Terceira nota({:.2f})\nSua média é ({:.2f})'.format(nota1,nota2,nota3,media))
print('Por isso, você está:')
if media >= 6.0:
    print('Aprovado!')
elif media < 6.0 and media > 4.0 :
    print('Exame Final!')
elif media < 4.0:
    print('Recuperação da Nota!')
