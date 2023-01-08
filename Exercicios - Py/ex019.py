"""        Exercício - 19 ( Sorteando um item na lista )
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. ...  """
"""...Faça um programa que ajude ele ,lendo o nome dela e escrevendo o nome do escolhido. ' """

import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Primeiro aluno: '))
n3 = str(input('Primeiro aluno: '))
n4 = str(input('Primeiro aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choices(lista)
print('O Aluno escolhido foi {}'.format(escolhido))
