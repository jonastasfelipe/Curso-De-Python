# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas

# O que eu fiz
'''distância = float(input('Qual a distância da viagem? '))
if distância <= 200:
    valor1 = distância * 0.50
    print('O valor da passagem é R${:.2f}'.format(valor1))
else:
    valor2 = distância * 0.45
    print('O valor da passagem é R${:.2f}'.format(valor2))
'''

# Resolução do exercício
distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começão uma viagem de {}km.'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))


# Resolução 2
'''distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começãr uma viagem de {}Km.'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}.'.format(preço))
'''