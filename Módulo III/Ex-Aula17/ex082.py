'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
valores = list()
pares = list()
impares = list()
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
for i in valores:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(f'Os valores digitados foram: {valores}')
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')
