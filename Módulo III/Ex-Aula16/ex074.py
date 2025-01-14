#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint 
num = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Os números sorteados foram: ', end='')
for n in num:
    print(f'{n}', end=' ')
print(f'\nO maior número sorteado foi {max(num)}') 
print(f'O menor número sorteado foi {min(num)}')
#max e min são funções que retornam o maior e o menor valor de uma tupla respectivamente
