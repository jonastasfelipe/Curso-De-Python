#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos Dolarres ela pode comprar
print('Conversor de R$ para US$')
r = float(input('Quanto reais você tem? '))
d = r/5.35
print('O valor em reais é R$ {:.2f}. É possível comprar US$ {:.2f} dólares.'.format(r,d))