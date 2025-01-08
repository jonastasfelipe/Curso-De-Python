# Crie um programa que leia dois valores e mostre um 
# menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada 
# em cada caso.   
from time import sleep
opção = 0
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        print('A soma de {} + {} é igual á {}'.format(v1, v2, v1+v2))
    elif opção == 2:
        print('A multiplicação de {} x {} é igual á {}'.format(v1, v2, v1*v2))
    elif opção == 3:
        if v1 > v2:
            print('{} é maior que {}'.format(v1, v2))
        elif v2 > v1:
            print('{} é maior que {}'.format(v2, v1))
        else:
            print('{} é igual á {}'.format(v1, v2))
    elif opção == 4:
        print('Informe os números novamente: ')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...') 
    else:
        print('Opção inválida. Tente novamente')
    sleep(2)
print('Fim do programa! Volte sempre!')
