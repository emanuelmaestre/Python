"""        Exercício - 22 ( Analisador de Textos )
Crie um programa que leia o nome completo de uma pessoa e mostre:  """
"""- Quantas letras ao todo (sem considerar espaços."""
"""- Quantas letras tem o primeiro nome."""

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maíusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome), nome.count('')))

separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras!'.format(separa[0], len(separa[0], )))
