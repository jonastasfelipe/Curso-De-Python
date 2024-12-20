#Crie um algoritimo que leia um número e mosrte o seu dobro, triplo, e raiz quadrada
n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)
print('O valor é {}, o seu dobro é {}, o seu triplo é {} e a sua raiz quadrada é {:.3f}.'.format(n,d,t,r))