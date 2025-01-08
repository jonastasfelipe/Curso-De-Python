# faça um progrma que leia um ângulo qualquer e mostre na tela e valor do seno, 
# cosseno e tangente desse ângulo.

#import math
#a = int(input('O ângulo é: '))
#s = math.asin
#c = math.acos
#t = math.atan
#print('Seno: {}'.format(s))
#rint('Cosseno: {}'.format(c))
#rint('Tangente: {}'.format(t))

import math
a = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(a))#Tenho que converte o valor de âgulo para radiano para a função math.sin funcionar
print('O ângulo de {:.0f}° tem o SENO de {:.2f}'.format(a,s))
c = math.cos(math.radians(a))
print('O ângulo de {:.0f}° tem o COSENO de {:.2f}'.format(a,c))
t = math.tan(math.radians(a))
print('O ângulo de {:.0f}° tem a TANGENTE de {:.2f}'.format(a,t))