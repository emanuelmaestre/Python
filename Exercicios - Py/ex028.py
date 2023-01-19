"""        Exercício - 28 ( Jogo de Adivinhação )
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça ao
usuário tentar descobrir qual foi o numero escolhido pelo computador. O Programa deverá escrever na
tela se o usuario "venceu ou perdeu ?" """

from random import randint

computador = randint(0, 5)  # Faz o Computador "Pensar"

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei ? '))  # Jogador tenta adivinhar

if jogador == computador:
    print('Parabens! Você conseguiu me vencer! ')

else:
    print('Ganhei! Pensei no número {} e não no {} ! '.format(computador, jogador))
