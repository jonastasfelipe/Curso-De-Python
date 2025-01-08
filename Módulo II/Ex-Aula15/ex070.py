# Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    valor =  float(input('Valor do produto: R$'))
    cont += 1 # A cada novo produto cadastrado dentro do laço de repetição irá contar mais um 
    total += valor # Irá somar cada valor cadastrado no laço de repetição
    if valor > 1000:
        totmil += 1
    if cont == 1 or valor < menor: 
        menor = valor
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Gostaria de continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:10.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')