n = str(input('Qual é seu nome completo? ')).strip()
n1 = n.split()
print('O seu primeiro nome é \n{} \nE seu último nome é \n{}'.format(n1[0], n1[len(n1)-1]))
