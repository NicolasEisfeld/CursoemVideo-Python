from math import radians,sin,cos,tan
an = float(input('Digite o angulo que deseja: '))
se = sin(radians(an))
print('O angulo de {} tem o seno de {:.2f}'.format(an,se))
cos = cos(radians(an))
print('O angulo de {} tem o cosseno de {:.2f}'.format(an,cos))
tan = tan(radians(an))
print('O angulo de {} tem um tangente de {:.2f}'.format(an,tan))

