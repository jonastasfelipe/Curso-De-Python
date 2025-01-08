#Escreva um programa que leia um valor em metros e o exiba convertido em centimentros a milimetros
n = float(input('Metros a serem convertidos: '))
c = n*100
m = c*100
print('{}m, {}cm, {}mm'.format(n,c,m))