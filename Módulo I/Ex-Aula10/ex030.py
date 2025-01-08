#Crie um programa que leia um númeroo inteiro e mostre na tela se ele é PAR ou IMPAR.

num = int(input('Digite um número: '))
res = num % 2 # O resto '%' deve ser 0 se for par e 1 se for impar
if res == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é IMPAR'.format(num))
