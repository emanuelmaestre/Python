"""        Exercício - 35 ( Analisando o Triangulo V 1.0 )
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário ,
se elas podem ou não formar um triângulo."""

print('-=-'*20)
print('Analisador de triângulo ')
print('-=-'*20)
R1 = float(input('Primeiro Segmento:'))
R2 = float(input('Segundo Segmento:'))
R3 = float(input('Terceiro Segmento:'))
if R1 < R2 + R3 and R2 < R1 + R3 and R3 < R1 + R2:
    print('Os segmentos acima podem formar triângulos!')
else:
    print('Os segmentos acima não podem formar triângulos')
    