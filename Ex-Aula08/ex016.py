#Crie um programa que leia um número Real qualquer pelo teclado e mostre na 
# tela a sua porção inteira 

from math import floor
n = float(input('Digite um número: '))
r = floor(n)
print('O número {} tem a parte inteira {}'.format(n, r))
