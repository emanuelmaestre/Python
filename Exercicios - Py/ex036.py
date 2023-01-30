"""        Exercício - 36 ( Aprovando Empréstimo )
Escreva um programa para aprovar o empréstimo bancario para a compra de uma
casa . Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
- A prestação mensal,não pode exceder 30% do salário ou então o empréstimo será negado."""

casa = float(input('Qual o valor da casa: R$ '))
salario = float(input('Qual o valor do salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento:'))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar um casa de R${:.2f} em {} anos'.format(casa, anos, end=''))
print('a prestação será de R${:.2f} '.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
