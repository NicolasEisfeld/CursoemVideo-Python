resposta = 0
prinum = int(input('Digite o Primeiro Valor: '))
sennum = int(input('Digite o Segundo Valor: '))
while resposta !=5:
    print('Digite a resposta desejada:')
    print('''   [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior 
    [ 4 ] Novos Números
    [ 5 ] Sair Do Programa''')
    resposta = int(input('Qual conta você deseja fazer? '))
    if resposta == 1:
        resultado = prinum + sennum
        print('O resultado da conta {} + {}, que você escolheu foi: {}'.format(prinum, sennum, resultado))
    elif resposta == 2:
        resultado = prinum * sennum
        print('O resultado da conta {} x {}, que você escolheu foi: {}'.format(prinum, sennum,resultado))
    elif resposta == 3:
        if prinum > sennum:
            resultado = prinum
        elif sennum > prinum:
            resultado = sennum
        print('O resultado da conta que você escolheu foi: {}'.format(resultado))
    elif resposta == 4:
        prinum - prinum
        sennum - sennum
        prinum = int(input('Digite o Primeiro Valor: '))
        sennum = int(input('Digite o Segundo Valor: '))
    elif resposta == 5:
        print('Tchau então :^( ')
    else:
        print('Opção Invalida! Tente Novamente...')