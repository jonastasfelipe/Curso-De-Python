#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    print('-'*35)
    escolha = int(input('Digite um número entre 0 e 20: '))
    print('-'*35)
    
    if escolha >= 0 and escolha <= 20:
        print(f'Você digitou o número {numero[escolha]}')
        break
    else:
        print('\nNúmero inválido. Tente novamente.\n')