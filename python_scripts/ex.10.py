# Faça um programa que leia a largura e a altura de uma parede em metro,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimesão de {} X {} e sua área e de {}m².'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede , você precisará de {}L de tinta.'.format(tinta))



