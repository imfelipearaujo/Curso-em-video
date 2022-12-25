#Exercício 011 - Pintando Parede
print('Exercício 011 - Pintando Parede.')
larg = float(input('Digite a largura da parede:'))
alt = float(input('Digite a altura da parede:'))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))
