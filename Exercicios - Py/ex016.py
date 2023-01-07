"""        Exercício - 16 ( Quebrando um número )
Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua superfície...  """
"""...c/ a sua porção inteira. Ex: ' Digite um número: 6.127. O número 6.127 tem a parte inteira 6. ' """

import math
num = float(input('Digite um valor: '))
print('O valor foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))
