"""        Exercício - 20 ( Sorteando uma ordem na lista )
O Mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos...  """
"""...Faça um programa que leia os nomes dos quatros alunos e mostre a ordem,sorteado. ' """

import random

n1 = str(input('1º Aluno: '))
n2 = str(input('2º Aluno: '))
n3 = str(input('3º Aluno: '))
n4 = str(input('4º Aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação: ')
print(lista)
