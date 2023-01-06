"""          Exercício - 04 (Dissecando uma variável)
Faça um programa que Leia algo pelo teclado e mostre na tela o
seu tipo primitivo e todas as informações possíveis sobre ele."""

a = input('Digite um valor:')
print(type(a))
print('Só tem espaços ?', a.isspace())
print('É um número?', a.isnumeric())
print('É um alfabeto?', a.isalpha())
print('É um alfanumérico ?', a.isalnum())
print('Está em maiúscula?', a.isupper())
print('Está em minúscula?', a.islower())
print('Está capitalizada?', a.istitle())
