"""        Exercício - 10 ( Conversos de Medidas )
Crie um programa que leia quanto mostre quantos dolares ela pode comprar."""
""" - Considere US$ 1,00 = R$ 3,27 """

real = float(input('Quanto dinheiro você tem na carteira ? '))
dolar = real / 3.27
print('com R$ {:.2F} você pode comprar US$ {:.2F}'.format(real, dolar))
