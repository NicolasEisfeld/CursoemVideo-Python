L = float(input('Largura da parede:'))
A = float(input('Altura da parede:'))
D = L * A
P = D / 2
print('Sua parede tem a dimensão de{}x{} e sua área é de {}m2\n Para pintar essa parede, você precisará de {}l de tinta'.format(L,A,D,P))