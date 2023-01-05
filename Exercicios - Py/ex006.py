"""        Exercício - 06 ( Dobro, Triplo, Raiz Quadrada )
Crie um algoritimo que leia e mostre o seu dobro ,triplo e raiz quadrada."""

n = int(input('Digite um número:'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O Dobro de {} é igual {}.'.format(n, d))
print('O Triplo de {} é igual {}.'.format(n, t))
print('A Raiz quadrada de {} é igual {:.0f}'.format(n, t, n, r))
