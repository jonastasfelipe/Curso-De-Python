#Escreva um proframa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu

#O que eu fiz
#import random
#num = random.randint(0,5)
#us = int(input('Qual o número escolhido pelo computador de 0 a 5? '))
#if us == num:
#   print('Você acertou!!')
#else:
#   print('Você errou!!')

#Resolução
from random import randint
from time import sleep
computador = randint(0,5) #faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # O Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3) # Esse comando faz o programa ter um delay de 3seg que é o tempo que está entre parenteses
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
