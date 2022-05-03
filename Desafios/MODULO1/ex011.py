larg = float(input('Digite a largura da sua parede: '))
alt = float(input('Digite a altura da sua parede: '))

area = larg * alt

print('A area da sua parede é de {}x{}, sendo então {}m².'.format(larg, alt, area))

tinta = area / 2

print('Você precisará de {}l de tinta.'.format(tinta))
