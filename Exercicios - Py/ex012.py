"""        Exercício - 12 ( Calculando descontos )
Faça um algoritimo que leia o preço de um produto e mostre seu novo preço,com 5% de desconto... """

preco = float(input('Qual é o preço do produto ? '))
novo = preco - (preco * 5 / 100)
print('O produto que custava R$ {:.2f} ,na promoção com desconto de 5% vai custar R$ {:.2F}'
      .format(preco, novo))
