# Faça um programa que leia o comprimento do cateto oposto e do cateto 
# adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

#import math
#o = float(input('O valor do cateto oposto: '))
#a = float(input('O valor do cateto adjacente: '))
#r1 = math.exp2(o)
#r2 = math.exp2(a)
#r3 = math.sqrt(r1+r2)
#print('O comprimento da hipotenusa é {:.3f}'.format(r3))

from math import hypot
o = float(input('Comprimento do cateto oposto: '))
a = float(input('Comprimento do cateto adjacente: '))
h = hypot(o,a)
print('A hipotenusa vai medir {:.2f}'. format(h))

