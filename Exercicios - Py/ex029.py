"""        Exercício - 29 ( Radar )
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h,
 mostre uma mensagem dizendo que foi multado. A multa vai custar R$ 7,00 por cada KM acima do limite"""

velocidade = float(input('Qual a velocidade atual do carro ? '))

if velocidade > 80:
    print('MULTADO! Você excedeu o limete permitido que é de 80 Km/h')

    multa = (velocidade - 80) * 7

    print('Você deve pagar uma multa de R$ {:.2f}!'.format(multa))
    print('Tenha um Bom dia! Dirija com segurança!')
