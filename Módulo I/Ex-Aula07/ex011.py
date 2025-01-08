#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área 
# e quantidade de tinta necessária para pintá-lo, sabendo que cada litro de tinta, 
# pinta uma área de 2m²
n1 = int(input('Largura da parede: '))
n2 = int(input('Altura da parede: '))
a = n1*n2
t = int(a/2)
print('A área é {}m², vai precisar de {} baldes de tinta para pintar a parede'.format(a,t))
