#  Crie um programa que faça o computador jogar Jokenpô com você.


#import random
#from time import sleep
#lista = ['PEDRA', 'PAPEL', 'TESOURA']
#computador = random.choice(lista)
#print(computador)
#print('''Suas opções:
#[ 0 ] PEDRA
#[ 1 ] PAPEL
#[ 2 ] TESOURA ''')
#opção = int(input('Qual é a sua jogada? '))
#print('JO')
#sleep(1)
#print('KEN')
#sleep(1)
#print('Pô!!!')
#if opção == 0 and computador == 'PAPEL':
#    print('''Computador jogou PAPEL
#Jogador jogou PEDRA''')
#    print('COMPUTADOR GANHOU')
#elif opção == 0 and computador == 'TESOURA':
#    print('''Computador jogou TESOURA
#Jogador jogou PEDRA''')
#    print('JOGADOR GANHOU')
#elif opção == 0 and computador == 'PEDRA':
#    print('''Computador jogou PEDRA
#Jogador jogou PEDRA''')
#    print('EMPATE! Jogue novamente!')
#elif opção == 1 and computador == 'PAPEL':
#    print('''Computador jogou PAPEL
#Jogador jogou PAPEL''')
#    print('EMPATE! Jogue novamente!')
#elif opção == 1 and computador == 'TESOURA':
#    print('''Computador jogou TESOURA
#Jogador jogou PAPEL''')
#    print('COMPUTADOR GANHOU')
#elif opção == 1 and computador == 'PEDRA':
#    print('''Computador jogou PEDRA
#Jogador jogou PAPEL''')
#    print('JOGADOR GANHOU')
#elif opção == 2 and computador == 'PAPEL':
#    print('''Computador jogou PAPEL
#Jogador jogou TESOURA''')
#    print('JOGADOR GANHOU')
#elif opção == 2 and computador == 'TESOURA':
#    print('''Computador jogou TESOURA
#Jogador jogou TESOURA''')
#    print('EMPATE! Jogue novamente!')
#elif opção == 2 and computador == 'PEDRA':
#    print('''Computador jogou PEDRA
#Jogador jogou TESOURA''')
#    print('COMPUTAOR GANHOU')

## RESOLUÇÃO DO EXERCÍCIO
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('Qual é a sua jogada? '))
print('=-=' * 10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=-=' * 10)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')    
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!') 
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!') 