# Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.
'''
totmaior = 0
totmenor = 0
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa:'.format(c)))
    if peso > peso:
        totmaior += 1
    else:
        totmenor += 1
print('O maior peso foi {}'.format(totmaior))
print('O menor peso foi {}'.format(totmenor))        
'''

# RESOLUÇÂO
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
