#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
p = float(input('Preço do produto: '))
q = p*0.05
s = p-q
print('O valor do produto é R$ {:.2f}, com o desconto de 5%, fica R$ {:.2f}.'.format(p,s))