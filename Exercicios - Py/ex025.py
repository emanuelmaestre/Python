"""        Exercício - 26 ( Procurando uma string dentro de uma string )
Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome """

nome = str(input('Qual é o seu nome completo ?')).strip()

print('Seu nome tem Silva {}'.format('Silva' in nome.lower()))
