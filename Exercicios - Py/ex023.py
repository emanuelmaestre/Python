"""        Exercício - 23 ( Separando digitos de um número )
Faça um programa que leia um número de 0 a 9999 e mostre nas telas cada um dos digitos separados.  """
""" Ex: Digite um número: 1834"""
"""Unidade: 4 / Dezena: 3 / Centena: 8 / Milhar: 1"""

num = int(input('Informe um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
