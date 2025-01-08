# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
# quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint #Bibliteca "RANDOM" com a função "RANDINT" fazendo a variável escolher de forma aleatória um número inteiro limitado aos números dentro dos "()"
v = 0
while True: #Irá repetir até ser interrompido pela função "break"
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU! Deu PAR')
            v += 1
        else:
            print('VOCÊ PERDEU! Deu IMPAR')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU! Deu IMPAR')
            v += 1
        else:
            print('VOCÊ PERDEU! Deu PAR')
            break
    else:
        print('Resposta inválida')
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
