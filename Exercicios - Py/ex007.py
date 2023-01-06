"""    Exercício - 07 ( Média Aritimética )
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média."""

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2
print('A Média entre {:.0f} e {:.0f} é igual a {:.0f}' .format(n1, n2, m))
