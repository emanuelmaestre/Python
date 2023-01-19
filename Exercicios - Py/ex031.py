"""        Exercício - 31 ( Custo da Viagem )
Desenvolva um programa que pergunte a distancia de uma viagem em KM. Calcule o preço da passagem,
cobrando R$ 0,50 por Km por viagens de até 200 Km e R$ 0,45 para viagens mais longas."""

distancia = float(input('Qual é a distancia da sua viagem ?'))
print('Você está prestes a começar uma viagem de {} Km.'.format(distancia))

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R$ {:.2f}!'.format(preco))
