larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, area))
print('A quantidade necessária de tinta para pintar esta parede é de: {} litros'.format(tinta))