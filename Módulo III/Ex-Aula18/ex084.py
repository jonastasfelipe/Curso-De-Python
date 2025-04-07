#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
temp = []
princial = []
maior = menor = 0
while True:
    temp.append(str(input('Nome:')))
    temp.append(float(input('Peso: ')))
    if len(princial) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princial.append(temp[:])
    temp.clear()
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
print('-='*30)    
print(f'Os dados foram {princial}')
print(f'Foram cadastradas {len(princial)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in princial:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in princial:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')        
