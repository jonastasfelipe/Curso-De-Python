#  Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número 
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False 
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez')
print('Acertou com {} tentativas'.format(palpite))
