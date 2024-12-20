#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
#custa R$60.00 por dia e R$0.15 po Km rodado
k = float(input('Km percorridos: '))
d = int(input('Dias alugados: '))
p = (60*d)+(0.15*k)
print('O total a pagar é de R${}'.format(p))