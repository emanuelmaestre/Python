"""        Exercício - 30 ( Par ou Impar )
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR!"""

numero = int(input('Me diga um número qualquer!'))

resultado = numero % 2

if resultado == 0:
    print('O número {} é PAR!'.format(numero))

else:
    print('O numero {} é IMPAR!'.format(numero))
