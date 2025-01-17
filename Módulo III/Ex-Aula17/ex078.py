# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
num = list()
for cont in range(0,5):
    num.append(int(input('Digite um valor: ')))
print(f'A lista foi criada com os determinados valores: {num}')
maior = max(num)
menor = min(num)
print(f'O maior valor digitado foi {maior} na posição ', end='')
for c, v in enumerate(num):
    if v == maior:
        print(f'{c} ', end='')
print(f'\nO menor valor digitado foi {menor} na posição ', end='')
for c, v in enumerate(num):
    if v == menor:
        print(f'{c} ', end='')
######################################################

    