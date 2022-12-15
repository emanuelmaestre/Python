"""              Exercício - 03 (Somando dois números)
Crie um programa que leia dois números e mostre a soma entre eles."""

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
n = int(n1 + n2)
print('A Soma dos números {} + {} é {}'.format(n1, n2, n))

#Cada chave "{}" que for mencionada dentro de print é necessario colocar um valor,
#...dentro deste valor será interligado com o que colocar dentro do format,ou seja,
#...se tem três chaves automaticamente terá que colocar 3 valores,porque se não ,ele
#...não irá apresentar a soma que foi solicitada!
