"""        Exercício - 33 ( Maior e Menor Valores )
Faça um programa que leia três numeros e mostre qual é o maior e qual é o menor."""

A = int(input('Primeiro Valor: '))
B = int(input('Segundo Valor: '))
C = int(input('Terceiro Valor: '))

# Verificando quem é o menor!

menor = A
if B < A and B < C:
    menor = B

if C < A and C < B:
    menor = C

# Verificando quem é o maior

maior = A
if B > A and B > C:
    maior = B

if C > A and C > B:
    maior = C

print('O menor valor digitado foi {}!'.format(menor))
print('O maior valor digitado foi {}!'.format(maior))
