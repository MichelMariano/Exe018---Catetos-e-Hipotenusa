
# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

#forma matemática de criar as coisas, forma tradicional:

'''
co = float(input('Comprimento do Cateto oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)

print('A Hipotenusa vai medir {:.2f}'.format(hi))
'''

#O mesmo exercicio, mas agora importando a classe ".math"
import math
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hi = math.hypot(co, ca)
print('A Hipotesuna vai medir {:.2f}'.format(hi))
