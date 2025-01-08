#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

#Forma simples ultilizando a biblioteca math
'''from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {}! é {}.'.format(n, f))'''

#Pelo método 'while'
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='') # O (, end='') é para não pular de linha
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    #print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

#Pelo método 'for'
'''n = int(input('Digíte um número para calcular seu fatorial: '))
c = n 
f = 1
print('Calculando {}! = '.format(n), end='')
for c in range(c, 0, -1):
    print('{}'.format(c), end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''
