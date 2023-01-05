"""                         Exercício - 08 ( Conversor de Medidas )
Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros."""

medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print('A Medida {:.0f}m corresponde a {:.0f}cm e {:.0f}mm '.format(medida, cm, mm))
