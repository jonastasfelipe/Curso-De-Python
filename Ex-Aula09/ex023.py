#Faça um programa que leia um número de 0 9999 e mostre na tela cada um dos dígitos separados.
#Ex: Digite um número: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

#Com string
#num=(input('Digite um número de 4 dígitos: '))
#print('Alalizando o número {}'.format(num))
#print('Unidade: {}'.format(num[3]))
#print('Dezena: {}'.format(num[2]))
#print('Centena: {}'.format(num[1]))
#print('Milhar: {}'.format(num[0]))

#Matemático
num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))