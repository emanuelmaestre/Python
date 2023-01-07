"""        Exercício - 11 ( Pintando Paredes )
Faça um programa que leia a largura e a altura de uma parede para pinta-lá... """
"""...sabendo que cada lata de tinta pinta uma area de 2m²."""

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2
print('Sua parede tem a dimensão de {:.0f}x{:.0f} m e sua área é de {:.0f}m².'.format(larg, alt, area))
print('Para pintar essa parede,você precisará de {}L de tinta.'.format(tinta))
