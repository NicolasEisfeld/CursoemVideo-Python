nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em Maiúsculas fica :', nome.upper())
print('Seu nome em Minusculas fica :', nome.lower())
print('Seu nome completo tem o total de: ', len(nome) - nome.count(' '), 'Caracteres')
print('Seu nome tem {} letras'.format(nome.find(' ')))

