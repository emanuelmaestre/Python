"""        Exercício - 15 ( Aluguel de Carros )
Escreva um programa que pergunte a quantidade de KM percorrido por um carro alugado e a quantidade...  """
""""...de dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$ 60,00... """
""""... p/ dia e R$ 0,15 p/ KM rodado."""

dias = int(input('Quantos dias alugados ? '))
km = float(input('Quantos Km rodados ? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R$ {:.2f}'.format(pago))
